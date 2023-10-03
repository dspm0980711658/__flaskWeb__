from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<H2>開始 FLASK  Go! </H2><p>Hello, FLASK  World!</p>"
@app.route('/hello_word')
def hello_word():
    return 'Hello, This is in Hello Word'