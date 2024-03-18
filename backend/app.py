from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*")

@app.route("/lazi", methods=['GET'])
def authors():
    return jsonify(
        {
            "authors": [
                "Karunia Syukur Baeha (10023478)",
                "William Manuel Kurniawan (13520035)",
                "Damianus Clairvoyance Diva Putra (13520035)"
            ]
        }
    )

@app.route("/lazi_encrypt", methods=['POST'])
def encrypt():
    plaintext = request.json
    return jsonify(
        {
            "encrypted": plaintext
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)