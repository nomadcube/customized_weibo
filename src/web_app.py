from flask import Flask

app = Flask(__name__)


@app.route("/<sentence>")
def hello(sentence):
    return repr(sentence)
app.run()
