"""Render the static travel pages from curated public JSON. Python stdlib only."""
from pathlib import Path
from html import escape
import json, re
ROOT=Path(__file__).resolve().parent.parent
TRAVEL=ROOT/'travel'


def e(text):
    return escape(str(text),quote=True)


def image(photo,large=False,eager=False,extra=''):
    w,h=photo['width'],photo['height']
    sw=round(w*min(1,640/max(w,h)));lw=round(w*min(1,2000/max(w,h)))
    return f'<img src="{e(photo["large"] if large else photo["small"])}" srcset="{e(photo["small"])} {sw}w, {e(photo["large"])} {lw}w" sizes="{extra or "(max-width: 700px) 100vw, (max-width: 1000px) 50vw, 400px"}" width="{w}" height="{h}" alt="{e(photo["caption"])}" loading="{"eager" if eager else "lazy"}" decoding="async"{chr(32)+"fetchpriority=high" if eager else ""}>'


def head(title,description,page):
    return f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{e(description)}"><meta name="theme-color" content="#0e3a5d">
<meta name="referrer" content="strict-origin-when-cross-origin"><title>{e(title)}｜MNFE2O4</title>
<link rel="stylesheet" href="../style.css"><link rel="stylesheet" href="vendor/leaflet/leaflet.css"><link rel="stylesheet" href="travel.css">
<script src="vendor/leaflet/leaflet.js" defer></script><script src="data/offline-map.js" defer></script><script src="data/trips.js" defer></script><script src="travel.js" defer></script>
</head><body class="travel-page" data-page="{e(page)}"><a class="skip-link" href="#main-content">跳转到主要内容</a>
<header class="travel-header"><a class="travel-brand" href="../index.html">MNFE2O4<span> / 旅行手记</span></a>
<nav aria-label="主导航"><a href="../index.html">首页</a><a href="index.html" aria-current="{'page' if page=='index' else 'true'}">旅行</a><a href="../index.html#works">文章</a><a href="../about.html">关于我</a></nav></header>'''


def footer():
    return '''<footer class="travel-footer"><a href="../index.html">MNFE2O4</a><span>把走过的路，慢慢留下来。</span><a href="index.html">回到旅行目录 ↑</a></footer>
<dialog class="photo-dialog" aria-label="照片查看器"><div class="lightbox-top"><span id="photo-counter" aria-live="polite"></span><button class="lightbox-close" type="button" aria-label="关闭照片">关闭 ×</button></div><div class="lightbox-stage"><button class="lightbox-prev" type="button" aria-label="上一张照片">‹</button><img class="lightbox-image" alt=""><button class="lightbox-next" type="button" aria-label="下一张照片">›</button></div><div class="lightbox-bottom"><p class="lightbox-caption"></p><span class="lightbox-meta"></span></div></dialog></body></html>'''


def tile(trip):
    cover=next(p for p in trip['photos'] if p['key']==trip['coverPhoto'])
    return f'''<article class="trip-tile"><a class="trip-cover" href="{trip['id']}.html">{image(cover,large=True,extra='(max-width: 720px) calc(100vw - 32px), 560px')}<span class="trip-cover-label">{e(trip['country'])}</span></a><div class="trip-tile-body"><p class="small-eyebrow">{e(trip['english'])} <span>{e(trip['dateLabel'])}</span></p><h3><a href="{trip['id']}.html">{e(trip['title'])}<span aria-hidden="true">↗</span></a></h3><p>{e(trip['intro'])}</p><div class="trip-tile-meta"><span>{e(trip['transportLabel'])}</span><span>{len(trip['photos'])} 张记忆</span></div></div></article>'''


def home(data):
    y,v=data['trips'];cover=next(p for p in y['photos'] if p['key']==y['coverPhoto']);aside=next(p for p in v['photos'] if p['key']=='V360')
    text=head('旅行手记','用地图、照片与原文游记，记录黄石公园与温哥华的旅程。','index')
    text+=f'''<main id="main-content" class="travel-main"><section class="travel-home-hero"><div class="home-hero-copy"><p class="small-eyebrow">PLACES, PATHS & MEMORIES</p><h1>走过的路，<br>留下的风景。</h1><p class="home-intro">有些记忆在目的地，<br>有些就藏在前往那里的路上。</p><a class="primary-link" href="#journeys">翻开旅行手记 <span aria-hidden="true">↓</span></a><div class="home-stats"><div><strong>{len(data['trips']):02}</strong><span>段旅程</span></div><div><strong>{sum(len(t['photos']) for t in data['trips'])}</strong><span>张精选照片</span></div><div><strong>2025</strong><span>这一年的远行</span></div></div></div><div class="home-hero-photos"><figure class="hero-photo-main">{image(cover,large=True,eager=True,extra='(max-width: 700px) 100vw, 700px')}<figcaption>01 / 黄石公园 · 大棱镜温泉</figcaption></figure><figure class="hero-photo-aside">{image(aside,large=True)}<figcaption>02 / 温哥华 · 秋日的海湾</figcaption></figure><span class="hero-photo-index" aria-hidden="true">45° N — 49° N</span></div></section>
<section class="overview-section" aria-labelledby="overview-heading"><div class="section-title-row"><div><p class="small-eyebrow">ON THE MAP</p><h2 id="overview-heading">两段旅程，放回地图里</h2></div><p class="section-aside">点地图上的地点，打开对应的手记。</p></div><div class="overview-map map-canvas" id="overview-map" role="region" aria-label="黄石公园与温哥华的旅行地图"></div><div class="overview-fallback"><a href="yellowstone.html">美国 · 黄石公园</a><span> / </span><a href="vancouver.html">加拿大 · 温哥华</a></div></section>
<section id="journeys" class="journeys-section"><div class="section-title-row"><div><p class="small-eyebrow">TRAVEL JOURNALS</p><h2>已经翻开的手记</h2></div><div class="home-filters" role="group" aria-label="按旅行地区筛选"><button type="button" data-country="all" aria-pressed="true">全部</button><button type="button" data-country="美国" aria-pressed="false">美国</button><button type="button" data-country="加拿大" aria-pressed="false">加拿大</button></div></div><div class="trip-grid">'''
    for trip in data['trips']:
        text+=f'<div data-trip-country="{e(trip["country"])}">{tile(trip)}</div>'
    text+='</div></section><section class="archive-section"><details><summary><span>还有一些旅程，正在慢慢整理</span><span class="archive-count">19 段记录 ＋</span></summary><p class="muted">以下是已有素材的旅行目录，路线与照片会逐次补上。</p><ol class="archive-list">'
    for trip in sorted(data['archive'],key=lambda t:t['startDateCandidate'],reverse=True):
        label='日期待核实' if trip['status']=='date-to-verify' else trip['startDateCandidate']+' — '+trip['endDateCandidate']
        text+=f'<li><span>{e(trip["title"])}</span><time>{e(label)}</time><span class="muted">待整理</span></li>'
    return text+'</ol></details></section></main>'+footer()


def transfers(trip,places):
    modes={'flight':'航班','train':'铁路','bus':'巴士','car':'汽车','walk':'步行','activity':'停留'}
    text=f'<details id="transit" class="itinerary-fold transfer-fold"><summary><span>往返交通</span><span class="fold-count">{len(trip["transfers"])} 段</span></summary><div class="fold-body"><table class="transfer-table"><caption class="visually-hidden">往返交通与班次</caption><thead><tr><th scope="col">日期</th><th scope="col">路段</th><th scope="col">交通 / 班次</th></tr></thead><tbody>'
    for leg in trip['transfers']:
        label=e(leg['dateLabel'])
        if '—' in label:
            a,b=label.split('—',1);label=a+'<br>—'+(b[3:] if a[:3]==b[:3] else b)
        text+=f'<tr class="transfer-leg"><td><time datetime="{e(leg["date"])}">{label}</time></td><td>{e(places[leg["from"]]["name"])} <span class="route-arrow" aria-hidden="true">→</span> {e(places[leg["to"]]["name"])}</td><td><span class="transport-tag mode-{leg["mode"]}">{modes[leg["mode"]]}</span><span class="transfer-service">{e(leg["service"])}</span></td></tr>'
    return text+'</tbody></table></div></details>'


def route_section(trip,places):
    text='<section id="route" class="route-section"><div class="section-title-row"><div><p class="small-eyebrow">THE JOURNEY</p><h2>沿着记忆，再走一遍</h2></div><p class="section-aside">选择一天，联动地图与照片。</p></div><div class="day-controls" role="group" aria-label="选择旅行日期"><button type="button" data-day="all" aria-pressed="true">完整行程</button>'
    for index,day in enumerate(trip['days'],1):
        text+=f'<button type="button" data-day="{e(day["date"])}" aria-pressed="false"><span>DAY {index:02}</span> {day["date"][5:].replace("-",".")}</button>'
    text+='</div><p id="route-active-summary" class="route-active-summary" aria-live="polite"></p><div class="route-layout"><div class="route-map-wrap"><div id="trip-map" class="map-canvas trip-map" role="region" aria-label="旅行停留点与路线地图"></div><div class="map-toolbar"><button type="button" data-map-action="all">全程往返</button>'
    text+=f'<button type="button" data-map-action="focus">{"园区细看" if trip["id"]=="yellowstone" else "市区细看"}</button></div><div class="map-photo-control"><button type="button" data-map-action="photos" aria-pressed="true">照片位置</button><span id="map-photo-hint" aria-live="polite">放大地图查看照片</span></div><p class="map-message" aria-live="polite"></p><div class="map-legend"><span><i class="legend-line"></i>{"自驾路线" if trip["id"]=="yellowstone" else "公共交通"}</span>'
    if trip['id']=='vancouver':
        text+='<span><i class="legend-line bike"></i>环园骑行</span><span><i class="legend-line ferry"></i>SeaBus 返程</span>'
    text+='<span><i class="legend-line flight"></i>航班</span><span><i class="legend-line train"></i>铁路接驳</span></div><p class="route-caption">路线为示意，航班连线非实际飞行轨迹。</p></div><aside class="itinerary-panel" aria-label="行程与地点">'+transfers(trip,places)+'<h3 class="route-places-heading">路上的停留点</h3><p id="route-day-summary">点击地点，在地图上定位。</p><ol class="stop-list">'
    for index,stop in enumerate(trip['stops'],1):
        text+=f'<li data-stop-row="{e(stop["id"])}"><button type="button" class="stop-button" data-stop="{e(stop["id"])}"><span class="stop-number">{index:02}</span><span>{e(stop["name"])}<small>{e(stop["english"])}</small></span><span aria-hidden="true">↗</span></button></li>'
    return text+'</ol></aside></div></section>'


def days(trip,places):
    text=f'<section id="days" class="days-section"><details class="days-fold"><summary>每日记录 <span>{len(trip["days"])} 天</span></summary><div class="day-timeline">'
    for index,day in enumerate(trip['days'],1):
        shots=[p for p in trip['photos'] if p['date']==day['date']]
        text+=f'<article class="day-entry" id="day-{e(day["date"])}"><div class="day-date"><span>DAY {index:02}</span><time datetime="{e(day["date"])}">{day["date"][5:].replace("-",".")}</time></div><div class="day-entry-body"><div class="day-entry-heading"><h3>{e(day["title"])}</h3><span class="transport-tag">{e(day["transport"])}</span></div><p>{e(day["summary"])}</p>'
        if day['stops']:
            text+='<div class="stop-chips">'+'<span aria-hidden="true">→</span>'.join(f'<button type="button" data-stop="{sid}" data-stop-day="{day["date"]}">{e(places[sid]["name"])}</button>' for sid in day['stops'])+'</div>'
        if shots:
            text+='<div class="day-preview">'
            for photo in shots[:3]:
                text+=f'<button type="button" data-photo="{photo["id"]}" aria-label="查看照片：{e(photo["caption"])}">{image(photo,extra="(max-width: 720px) 30vw, 300px")}</button>'
            text+=f'</div><button type="button" class="text-button" data-show-gallery="{day["date"]}">看这一天的 {len(shots)} 张照片 <span aria-hidden="true">↗</span></button>'
        text+='</div></article>'
    return text+'</div></details></section>'


def gallery(trip,places):
    text='<section id="gallery" class="gallery-section"><div class="section-title-row"><div><p class="small-eyebrow">MOMENTS TO KEEP</p><h2>值得留下的画面</h2></div><div class="gallery-meta"><span id="gallery-count" aria-live="polite">'+str(len(trip['photos']))+' 张照片</span><button type="button" class="text-button" id="gallery-reset" hidden>显示全部</button></div></div><div class="gallery-active-filter" id="gallery-filter" aria-live="polite"></div><div class="photo-grid">'
    for index,photo in enumerate(trip['photos']):
        sizes='(max-width: 720px) calc((100vw - 44px)/2), (max-width: 899px) 30vw, '+('760px' if index%9==0 else '370px')
        text+=f'<figure class="gallery-item" data-photo-date="{photo["date"]}" data-photo-stop="{photo["stop"]}"><button type="button" class="gallery-open" data-photo="{photo["id"]}" aria-label="查看大图：{e(photo["caption"])}">{image(photo,extra=sizes)}<span class="photo-expand" aria-hidden="true">↗</span></button><figcaption><span>{e(photo["caption"])}</span><small>{photo["date"][5:].replace("-",".")} · {photo["time"]} <span>{e(photo.get("locationLabel",places[photo["stop"]]["name"]))}</span></small></figcaption></figure>'
    return text+'</div><p class="gallery-empty" hidden>暂无照片。</p></section>'


def essay(trip):
    text='<section id="essay" class="essay-section"><div class="essay-heading"><p class="small-eyebrow">NOTES FROM THE ROAD</p><h2>旅行随记</h2><p>'+e(trip['english'])+'</p></div><div class="essay-prose">'
    for para in re.split(r'\n\s*\n',trip['essay'].replace('\u200b','').strip()):
        if para.strip():text+='<p>'+e(para.strip()).replace('\n','<br>')+'</p>'
    return text+'</div></section>'


def detail(trip):
    tid=trip['id'];places={s['id']:s for s in trip['stops']};cover=next(p for p in trip['photos'] if p['key']==trip['coverPhoto'])
    text=head(trip['title']+'旅行手记',trip['intro'],tid)
    text+=f'''<main id="main-content" class="travel-main trip-main"><div class="trip-breadcrumb"><a href="index.html">旅行手记</a><span aria-hidden="true"> / </span><span>{e(trip['title'])}</span></div><section class="trip-hero">{image(cover,large=True,eager=True,extra='100vw')}<div class="trip-hero-shade"></div><div class="trip-hero-copy"><p class="small-eyebrow">{e(trip['english'])}</p><h1>{e(trip['title'])}</h1><p>{e(trip['quote'])}</p><div class="trip-hero-meta"><span>{e(trip['dateLabel'])}</span><span>{e(trip['transportLabel'])}</span></div></div><span class="trip-hero-caption">{e(cover['caption'])}</span></section>
<nav class="trip-anchor-nav" aria-label="旅行内容导航"><a href="#transit">往返交通</a><a href="#route">地图行程</a><a href="#days">每日记录</a><a href="#gallery">精选照片 <span>{len(trip['photos'])}</span></a><a href="#essay">旅行随记</a></nav>
<div class="trip-introduction"><p>{e(trip['intro'])}</p>'''
    if trip.get('dateNote'):text+=f'<p class="date-note">{e(trip["dateNote"])}</p>'
    text+='</div>'+route_section(trip,places)+days(trip,places)+gallery(trip,places)+essay(trip)
    other='vancouver' if tid=='yellowstone' else 'yellowstone';name='温哥华 · 秋色与海湾' if tid=='yellowstone' else '黄石公园 · 河谷与热泉'
    return text+f'<section class="next-journey"><p class="small-eyebrow">ANOTHER JOURNEY</p><a href="{other}.html">下一段旅程：{name} <span aria-hidden="true">↗</span></a></section></main>'+footer()


def main():
    data=json.loads((TRAVEL/'data/trips.json').read_text(encoding='utf-8'))
    (TRAVEL/'index.html').write_text(home(data),encoding='utf-8')
    for trip in data['trips']:(TRAVEL/(trip['id']+'.html')).write_text(detail(trip),encoding='utf-8')
    (TRAVEL/'data/trips.js').write_text('window.TRAVEL_DATA = '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    print('Rendered travel index, two trip pages and browser data.')


if __name__=='__main__':main()
