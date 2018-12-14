from flask import Flask, request
from flask import jsonify
import cloudpickle
import datetime

MODELS = dict()

# load sample model
with open('/app/notebook/models/sample/model.pkl', 'rb') as f:
    _model_pkl = f.read()
    _model = cloudpickle.loads(_model_pkl)
    MODELS.update({'sample': _model})


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return ''


@app.route('/health', methods=['GET'])
def health():
    return 'OK'


@app.route('/models/<model_name>/predict', methods=['POST'])
def predict(model_name):
    model = MODELS.get(f'{model_name}')
    result = model.format_predict(request.json)
    return jsonify({
        'now': f'{datetime.datetime.now()}',
        'model_name': model_name,
        'result': result.tolist(),
    })


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
