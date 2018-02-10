import os
from logging import INFO
from logging import basicConfig

from flask import Flask, jsonify, logging, send_from_directory
from flask_cors import CORS

from persistence import Persistence

app = Flask(__name__)
CORS(app)

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('../frontend/dist/', path)


@app.route('/log')
def hello():
    return read_file(os.environ['APP_LOG'])


def read_file(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open(path, 'r') as file:
        content = file.read()
    return content


@app.route('/tweets', methods=['GET'])
def tweet_list():
    from twitter_api import TwitterAPI
    t = TwitterAPI()
    t.set_query("cadiz", "36.528580", "-6.213026", "5")
    result = t.get_json() 
    #tweets = repository.list()
    #print results
    return result


if __name__ == '__main__':
    abs_path = os.path.dirname(os.path.abspath(__file__))
    log = os.path.join(abs_path, os.environ['APP_LOG'])
    basicConfig(filename=log, level=INFO)

    db = os.path.join(abs_path, os.environ['DB_PATH'])
    repository = Persistence(db, logging.getLogger(__name__))
    repository.init_db()

    app.run(host=os.environ['IP_LISTEN'], port=int(os.environ['PORT_LISTEN']), threaded=True)
