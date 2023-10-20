from flask import Flask, request


app = Flask(__name__)


@app.post("/upload")
def hello_world():
    with open('./media/file.txt', 'a') as file:
        files = request.files["file"]
        data = files.read().decode("utf-8")
        file.write(data)
    return {"message": "hello"}


@app.get("/")
def welcome():
    return "welcome"

