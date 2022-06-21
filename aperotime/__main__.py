#!/bin/python3

import sys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import argparse
from aperotime import is_this_apero_time

app = FastAPI()

@app.get("/")
def read_root():
    if is_this_apero_time():
        cocktail = randomize_cocktail()
        return {"aperotime": True, "drink": cocktail}
    else:
        return {"aperotime": False}

def main(host="127.0.0.1", port=8000):
    uvicorn.run(app, host=host, port=port)
    return 0

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8000

    parser = argparse.ArgumentParser(description="Aperotime server")
    parser.add_argument("--host", metavar="host", type=str, help="host address", default=host)
    parser.add_argument("--port", metavar="port", type=int, help="port", default=port)

    args = parser.parse_args()
    if args.host is not None:
        host = args.host
    if args.port is not None:
        port = args.port

    sys.exit(main(host, port))
