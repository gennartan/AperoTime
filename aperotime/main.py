from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

