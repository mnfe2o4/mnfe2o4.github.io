"""Validate the public travel data and generated assets (Python stdlib)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,math
ROOT=Path(__file__).resolve().parent.parent

class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if 'id' in attrs:self.ids.append(attrs['id'])
  if tag in ['a','link','img','script']:
   value=attrs.get('href') or attrs.get('src')
   if value:self.links.append(value)

def coordinate(point):
 return isinstance(point,list) and len(point)==2 and all(isinstance(n,(int,float)) and math.isfinite(n) for n in point) and -90<=point[0]<=90 and -180<=point[1]<=180

def main():
 data=json.loads((ROOT/'travel/data/trips.json').read_text(encoding='utf-8'));all_ids=set();photos=set();flight_codes=set()
 assert data['scopeEnd']=='2025-12-31'
 for trip in data['trips']:
  tid=trip['id'];assert tid not in all_ids;all_ids.add(tid)
  assert trip['dateStart']<=trip['dateEnd']<='2025-12-31',tid
  stops={s['id']:s for s in trip['stops']};assert len(stops)==len(trip['stops'])
  assert all(s.get('coordinates') is None or coordinate(s['coordinates']) for s in stops.values()),tid
  days={d['date'] for d in trip['days']};assert len(days)==len(trip['days'])
  assert all(trip['dateStart']<=d<=trip['dateEnd'] for d in days),tid
  assert all(s in stops for d in trip['days'] for s in d['stops']),tid
  assert trip['coverPhoto'] in [p['key'] for p in trip['photos']],tid
  assert coordinate(trip['overviewCoordinates']),tid
  for photo in trip['photos']:
   assert photo['id'] not in photos;photos.add(photo['id']);assert photo['stop'] in stops
   assert photo['date'] in days,(tid,photo['id'],photo['date'])
   assert photo.get('mapCoordinates') is None or coordinate(photo['mapCoordinates']),photo['id']
   assert photo['width']>0 and photo['height']>0
   for kind in ['small','large']:assert (ROOT/'travel'/photo[kind]).is_file(),photo[kind]
  for route in trip['routes']:
   assert route['day'] in days,(tid,route['day']);assert all(coordinate(p) for p in route['coordinates'])
   assert len(route['coordinates'])>=2
   for endpoint in ['from','to']:
    if route.get(endpoint):assert route[endpoint] in stops,(tid,route['id'],endpoint)
  assert len({r['id'] for r in trip['routes']})==len(trip['routes']),('Duplicate route IDs',tid)
  assert len({l['id'] for l in trip.get('transfers',[])})==len(trip.get('transfers',[])),('Duplicate transfer IDs',tid)
  for leg in trip.get('transfers',[]):
   assert leg['from'] in stops and leg['to'] in stops,(tid,leg)
   assert leg['date'] in days,(tid,leg['date'])
   if leg['mode']=='flight' and leg['service']:flight_codes.add(leg['service'])
  assert (ROOT/'travel'/(tid+'.html')).exists(),tid
 raw=json.dumps(data,ensure_ascii=False)
 assert not re.search(r'[A-Z]:[\\/]',raw),'Private filesystem path in public data'
 assert not any(term in raw for term in ['sourcePath','originalTimeRaw','本人补充','由本人确认','待核实','证据说明']),'Private/process fields in public data'
 assert len(flight_codes)==data['flightCount'],(len(flight_codes),data['flightCount'])
 for path in (ROOT/'travel').glob('*.html'):
  page=Page();page.feed(path.read_text(encoding='utf-8'));assert len(page.ids)==len(set(page.ids)),path
  for link in page.links:
   url=urlsplit(link)
   if url.scheme or url.netloc:continue
   target=path.parent/unquote(url.path) if url.path else path
   assert target.exists(),(path,link)
   if url.fragment and target.suffix=='.html':
    other=Page();other.feed(target.read_text(encoding='utf-8'));assert url.fragment in other.ids,(path,link)
 print(f'Validated {len(all_ids)} trips, {len(photos)} images, {len(flight_codes)} unique flights, local assets and anchors.')

if __name__=='__main__':main()
