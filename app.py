from flask import Flask
from flask import jsonify
from flask import request
from guessit import guessit

app = Flask(__name__)

def guess(filename):
    guess = guessit(filename)

    # Country is not unicode, it makes the jsonify crash...
    # I don't need it anyway so let's remove it
    if 'country' in guess:
        del guess['country']

    return jsonify(guess)

@app.route("/guess", methods=['POST'])
def guess_post():
    content = request.get_json()
    return guess(content['name'])

@app.route("/guess/<filename>", methods=['GET'])
def guess_get(filename):
    return guess(filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
