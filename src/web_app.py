from flask import Flask
from hdfs import InsecureClient
import codecs
import subprocess

app = Flask(__name__)


@app.route("/<sentence>")
def hello(sentence):
    hdfs_client = InsecureClient('http://127.0.0.1:50070')
    nearest_posts = None
    with hdfs_client.read('best_posts/part-00000') as reader:
        for line in reader:
            nearest_posts = codecs.decode(line.strip(), "utf-8")
    return nearest_posts


app.run()
