from flask import Flask, jsonify, request
app = Flask(__name__)

languages= [{'name':'javascript'}, {'name':'Java'},{'name':'python'}, 
{'name':'react-native'}, {'name':'C++'}]

@app.route('/', methods=['GET'])

def test():
    return jsonify({'message' :'It works'})


@app.route('/lang', methods=['GET'])
def returnlanguges():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnone(name):
    langs = [language for language in languages if language ['name']== name]
    return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
def addone():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editone(name):
    langs = [language for language in languages if language ['name']== name]
    langs[0]['name'] = request.json['name']
    return jsonify({'languages': langs[0]})



if __name__ =='__main__':
    app.run(debug=True)