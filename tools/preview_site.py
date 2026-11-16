"""Serve this checkout locally so online maps have a valid HTTP origin."""
from pathlib import Path
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from functools import partial
import argparse,webbrowser

ROOT=Path(__file__).resolve().parent.parent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=int,default=8000)
    parser.add_argument('--no-open',action='store_true')
    args=parser.parse_args()
    handler=partial(SimpleHTTPRequestHandler,directory=str(ROOT))
    try:server=ThreadingHTTPServer(('127.0.0.1',args.port),handler)
    except OSError:server=ThreadingHTTPServer(('127.0.0.1',0),handler)
    url=f'http://127.0.0.1:{server.server_port}/travel/'
    print('Local preview: '+url,flush=True)
    print('Press Ctrl+C to stop. This does not publish the site.',flush=True)
    if not args.no_open:webbrowser.open(url)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()


if __name__=='__main__':main()
