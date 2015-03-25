from flask import Flask
from flask import jsonify
from guessit import guess_file_info

app = Flask(__name__)

@app.route("/guess/<filename>")
def guess(filename):
    guess = guess_file_info(filename)

    # Country is not unicode, it makes the jsonify crash...
    # I don't need it anyway so let's remove it
    if 'country' in guess:
        del guess['country']

    return jsonify(guess)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
