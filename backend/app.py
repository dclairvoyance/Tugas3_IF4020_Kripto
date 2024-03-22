from flask import Flask, request, jsonify
from flask_cors import CORS
from delazi import ecb_encrypt, ecb_decrypt, cbc_encrypt, cbc_decrypt, cfb_encrypt, cfb_decrypt, \
                   ofb_encrypt, ofb_decrypt, counter_encrypt, counter_decrypt

app = Flask(__name__)
cors = CORS(app, origins="*")

@app.route("/delazi", methods=['GET'])
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

@app.route("/delazi_encrypt", methods=['POST'])
def delazi_encrypt_api():
    plaintext = request.json["plaintext"]
    key = request.json["key"]
    round = request.json["round"]
    mode = request.json["mode"]
    if (mode == "ofb" or mode == "cfb"):
        size = request.json["size"]
    if (mode == "ecb"):
        encrypted = ecb_encrypt(plaintext, key, round)
    elif (mode == "cbc"):
        encrypted = cbc_encrypt(plaintext, key, round)
    elif (mode == "cfb"):
        encrypted = cfb_encrypt(plaintext, key, round, size)
    elif (mode == "ofb"):
        encrypted = ofb_encrypt(plaintext, key, round, size)
    else:
        encrypted = counter_encrypt(plaintext, key, round)
    return jsonify(
        {
            "status": 200,
            "message": {
                "encrypted": encrypted
            }
        }
    )

@app.route("/delazi_decrypt", methods=['POST'])
def delazi_decrypt_api():
    ciphertext = request.json["ciphertext"]
    key = request.json["key"]
    round = request.json["round"]
    mode = request.json["mode"]
    if (mode == "ofb" or mode == "cfb"):
        size = request.json["size"]
    if (mode == "ecb"):
        decrypted = ecb_decrypt(ciphertext, key, round)
    elif (mode == "cbc"):
        decrypted = cbc_decrypt(ciphertext, key, round)
    elif (mode == "cfb"):
        decrypted = cfb_decrypt(ciphertext, key, round, size)
    elif (mode == "ofb"):
        decrypted = ofb_decrypt(ciphertext, key, round, size)
    else:
        decrypted = counter_decrypt(ciphertext, key, round)
    return jsonify(
        {
            "status": 200,
            "message": {
                "decrypted": decrypted
            }
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)