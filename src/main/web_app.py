from flask import Flask
from src.data_processing.processing import chinese_shingle, similarity


doc_set_path = '/Users/wumengling/PycharmProjects/customized_weibo/chinese'
app = Flask(__name__)


@app.route("/<sentence>")
def hello(sentence):
    new_doc = sentence.strip().split()
    doc_set = chinese_shingle(doc_set_path)
    largest_similarity = 0.0
    result_doc = ''
    for doc in doc_set:
        new_similarity = similarity(doc, new_doc)
        if new_similarity > largest_similarity:
            largest_similarity = new_similarity
            result_doc = doc
    return repr(largest_similarity) + repr(''.join(result_doc).encode('utf-8'))
app.run()
