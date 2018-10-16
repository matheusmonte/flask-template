#!flask/bin/python
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/research', methods=['GET'])
def get_sample():
    return jsonify({'What_is_it': 'Sample' })

@app.route('/api/login', methods=['POST'])
def post_sample():
    json_data = request.get_json(force=True)
    un = json_data['username']
    pw = json_data['password'] 
    #add check at database
    response = False
    if str(un) == 'clark' and str(pw) =='12345':
        response = True
    return jsonify({'response': response})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)