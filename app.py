from flask import Flask
from flask import jsonify
from guessit import guess_file_info

app = Flask(__name__)

@app.route("/guess/<filename>")
def guess(filename):
    return jsonify(guess_file_info(filename))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
