from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)

def read_json(file):
    with open(os.path.join(BASE_DIR, '..', 'data', file), encoding='utf-8') as f:
        return json.load(f)

@app.route("/api/phrases")
def get_phrases():
    return jsonify(read_json("phrases.json"))

@app.route("/api/propose", methods=["POST"])
def submit_proposal():
    data = request.json
    print("Proposition reçue :", data)
    return jsonify({"status": "ok", "message": "Proposition enregistrée"})
