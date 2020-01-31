from flask import Flask
from flask import jsonify
from flask import request
from guessit import guessit

app = Flask(__name__)

def guess(filename):
    guess = guessit(filename)

    # Remove the size
    if 'size' in guess:
        del guess['size']

    # Country is a babelfish object and cannot be marshaled into JSON. We're
    # not using the country anyway so let's append the country to the title.
    # This also fixes wrong country match in the filename.
    # e.g "Scandal.(US).S01E01.mp4" -> "Scandal US"
    # e.g "Us (2019).mp4"           -> "US"
    if 'country' in guess:
        country = str(guess['country'])
        if 'title' in guess:
            guess['title'] += ' ' + country
        else:
            guess['title'] = country

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
