#!/bin/python3

from datetime import datetime
import random
import sys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import argparse

def is_this_apero_time():
    now = datetime.now()

    if now.hour > 17 and now.minute > 30:
        return True
    else:
        return False

cocktail_list = [
        "gin tonic",
        "vodka",
        "rhum",
        "beer",
        "tequila",
        "soda",
        ]

def randomize_cocktail():
    return random.choice(cocktail_list)

app = FastAPI()

@app.get("/")
def read_root():
    if is_this_apero_time():
        cocktail = randomize_cocktail()
        return {"aperotime": True, "drink": cocktail}
    else:
        return {"aperotime": False}

def main(host="127.0.0.1", port=8000):

    parser = argparse.ArgumentParser(description="Aperotime server")
    parser.add_argument("--host", metavar='host', type=str, help="host address", default=host)
    parser.add_argument("--port", metavar='port', type=int, help="port", default=port)

    args = parser.parse_args()
    if args.host is not None:
        host = args.host
    if args.port is not None:
        port = args.port

    uvicorn.run(app, host=host, port=port)
    return 0

if __name__ == '__main__':

    sys.exit(main())

