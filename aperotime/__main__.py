#!/bin/python3

import sys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello", response_class=HTMLResponse)
def read_hello():
    return """<!DOCTYPE html>  
<html>
<head>
<title></title>
</head>

<body>
The content of the document......
</body>

</html> 
"""


def main():
    print("This is my main function")
    uvicorn.run(app, host="127.0.0.1", port=8000)
    return 0

if __name__ == '__main__':
    sys.exit(main())
