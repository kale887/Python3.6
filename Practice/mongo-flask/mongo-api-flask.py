from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'local'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/local'

mongo = PyMongo(app)


@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.framework

    output = []

    for q in framework.find():
        output.append({'name': q['name'], 'language': q['language']})

    return jsonify({'result': output})


@app.route('/framework/<name>', methods=['GET'])
def get_one_framework(name):
    framework = mongo.db.framework

    q = framework.find_one({'name': name})

    if q:
        output = {'name': q['name'], 'language': q['language']}
    else:
        output = 'No results found'

    return jsonify({'result': output})


# route () decorator trigger URL should trigger our function

@app.route('/framework', methods=['POST'])
def add_framework():
    framework = mongo.db.framework

    name = request.json['name']
    language = request.json['language']

    framework_id = framework.insert({'name': name, 'language': language})
    new_framework = framework.find_one({'_id': framework_id})

    output = {'name': new_framework['name'], 'language': new_framework['language']}

    return jsonify({'result': output})


# debug support the server will reload itself on code changes,
# and it will also provide you with a helpful debugger if things go wrong.
if __name__ == '__main__':
    app.run(debug=True)

    # If app.run(host= '0.0.0.0') this tells os to listen on all public IP's
