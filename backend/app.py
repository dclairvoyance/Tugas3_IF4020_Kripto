from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from delazi import ecb_encrypt, ecb_decrypt, cbc_encrypt, cbc_decrypt, cfb_encrypt, cfb_decrypt, \
                   ofb_encrypt, ofb_decrypt, counter_encrypt, counter_decrypt
import os

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
        encrypted, time = ecb_encrypt(plaintext, key, round)
    elif (mode == "cbc"):
        encrypted, time = cbc_encrypt(plaintext, key, round)
    elif (mode == "cfb"):
        encrypted, time = cfb_encrypt(plaintext, key, round, size)
    elif (mode == "ofb"):
        encrypted, time = ofb_encrypt(plaintext, key, round, size)
    else:
        encrypted, time = counter_encrypt(plaintext, key, round)
    return jsonify(
        {
            "status": 200,
            "message": {
                "encrypted": encrypted,
                "time": time
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
        decrypted, time = ecb_decrypt(ciphertext, key, round)
    elif (mode == "cbc"):
        decrypted, time = cbc_decrypt(ciphertext, key, round)
    elif (mode == "cfb"):
        decrypted, time = cfb_decrypt(ciphertext, key, round, size)
    elif (mode == "ofb"):
        decrypted, time = ofb_decrypt(ciphertext, key, round, size)
    else:
        decrypted, time = counter_decrypt(ciphertext, key, round)
    return jsonify(
        {
            "status": 200,
            "message": {
                "decrypted": decrypted,
                "time": time
            }
        }
    )

@app.route("/delazi_file_encrypt", methods=['POST'])
def delazi_file_encrypt_api():
    # if file not found
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    key = request.form["key"]
    round = int(request.form["round"])
    mode = request.form["mode"]
    if (mode == "ofb" or mode == "cfb"):
        size = int(request.form["size"])
    # if file not selected
    if file.filename == '':
        return "No selected file"
    if file:
        file_hex = ''.join(format(x, '02x') for x in file.read())
        if (mode == "ecb"):
            encrypted_hex, time = ecb_encrypt(file_hex, key, round)
            encrypted = bytes.fromhex(encrypted_hex)
        elif (mode == "cbc"):
            encrypted_hex, time = cbc_encrypt(file_hex, key, round)
            encrypted = bytes.fromhex(encrypted_hex)
        elif (mode == "cfb"):
            encrypted_hex, time = cfb_encrypt(file_hex, key, round, size)
            encrypted = bytes.fromhex(encrypted_hex)
        elif (mode == "ofb"):
            encrypted_hex, time = ofb_encrypt(file_hex, key, round, size)
            encrypted = bytes.fromhex(encrypted_hex)
        else:
            encrypted_hex, time = counter_encrypt(file_hex, key, round)
            encrypted = bytes.fromhex(encrypted_hex)

        file_path = os.path.join('encrypted', 'encrypted.txt')
        with open(file_path, 'wb') as f:
            f.write(encrypted)

        return send_file(file_path, as_attachment=True), {"time": time}

@app.route("/delazi_file_decrypt", methods=['POST'])
def delazi_file_decrypt_api():
    # if file not found
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    key = request.form["key"]
    round = int(request.form["round"])
    mode = request.form["mode"]
    if (mode == "ofb" or mode == "cfb"):
        size = int(request.form["size"])
    # if file not selected
    if file.filename == '':
        return "No selected file"
    if file:
        file_hex = ''.join(format(x, '02x') for x in file.read())
        if (mode == "ecb"):
            decrypted_hex, time = ecb_decrypt(file_hex, key, round)
            decrypted = bytes.fromhex(decrypted_hex)
        elif (mode == "cbc"):
            decrypted_hex, time = cbc_decrypt(file_hex, key, round)
            decrypted = bytes.fromhex(decrypted_hex)
        elif (mode == "cfb"):
            decrypted_hex, time = cfb_decrypt(file_hex, key, round, size)
            decrypted = bytes.fromhex(decrypted_hex)
        elif (mode == "ofb"):
            decrypted_hex, time = ofb_decrypt(file_hex, key, round, size)
            decrypted = bytes.fromhex(decrypted_hex)
        else:
            decrypted_hex, time = counter_decrypt(file_hex, key, round)
            decrypted = bytes.fromhex(decrypted_hex)

        file_path = os.path.join('decrypted', 'decrypted.txt')
        with open(file_path, 'wb') as f:
            f.write(decrypted)

        return send_file(file_path, as_attachment=True), {"time": time}

if __name__ == "__main__":
    app.run(debug=True, port=8080)