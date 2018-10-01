#!flask/bin/python
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/get', methods=['GET'])
def get_sample():
    return jsonify({'What_is_it': 'Sample' })

@app.route('/api/post', methods=['POST'])
def post_sample():
    if not request.json or not 'title' in request.json:
        abort(400)
    sample_object = {
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    
    return jsonify({'sample': sample_object}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)