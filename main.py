from fastapi import FastAPI,Path
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse

#create obj of class
app=FastAPI()

#decorator который будет обслуживать метод get
@app.get("/")
def root():
    return {"message": "Hello,student"}

@app.get("/add")
def add(x:int, y:int)->int:
    return x+y

@app.get("/double/{number}")
def double(number:int)->int:
    return number*2

#первой обрабатывается та ручка, которая написана в скрипте!
@app.get("/welcome/{name}")
def welcome(name:str=Path(min_length=2, max_length=20))->str:
    return f"Good luck, {name}!"

@app.get("/welcome/Anatun")
def welcome(name:str=Path(min_length=2, max_length=20))->str:
    return f"Good luck, {name}!"

@app.get("/phone/{number}")
def phone_number(number: str=Path(regex = "^\\+?[1-9][0-9]{7,14}$")):
    return {"phone":number}

#these three check not in postman but on localhost
@app.get("/text")
def get_text():
    content="Lorem ipsum"
    return PlainTextResponse(content=content)

'''@app.get("/html")
def get_html():
    content="<h1>Mobs</h1>"
    return HTMLResponse(content=content)
'''
@app.get("/file")
def get_file():
    content="index.html"
    return FileResponse(content,
                        media_type="application/octet-stream",
                        filename="index_2.html")
#media_type - нужен для того, чтоб файл не преобразовывался сразу
#filename - имя файла, который можно будет скачать, так как мы не преобразуем сразу

@app.get(path="/html", response_class=HTMLResponse)
def get_html():
    content="<h1>Mobs</h1>"
    return content