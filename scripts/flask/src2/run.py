from flask import Flask, request
from flask import jsonify
import datetime


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return ''


@app.route('/health', methods=["GET"])
def health():
    return 'OK'


@app.route('/params/path_param/<path_param>', methods=["GET"])
def get_path_param(path_param):
    return jsonify({
        'now': f'{datetime.datetime.now()}',
        'param': path_param,
    })


@app.route('/params/query_param', methods=["GET"])
def get_query_param():
    query_param = request.args.get('value')
    return jsonify({
        'now': f'{datetime.datetime.now()}',
        'param': query_param,
    })


@app.route('/params/request_body', methods=["POST"])
def get_request_body():
    request_body = request.json
    return jsonify({
        'now': f'{datetime.datetime.now()}',
        'param': request_body,
    })


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
