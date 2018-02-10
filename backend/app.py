import os
from logging import INFO
from logging import basicConfig

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return read_file(os.environ['APP_LOG'])


def read_file(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open(path, 'r') as file:
        content = file.read()
    return content


@app.route('/tweets', methods=['POST'])
def tweet_post():
    return jsonify('{}'), 201


@app.route('/tweets', methods=['GET'])
def tweet_list():
    return jsonify('{}')


if __name__ == '__main__':
    abs_path = os.path.dirname(os.path.abspath(__file__))
    log = os.path.join(abs_path, os.environ['APP_LOG'])
    basicConfig(filename=log, level=INFO)

    app.run(host=os.environ['IP_LISTEN'], port=int(os.environ['PORT_LISTEN']), threaded=True)