# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Aplicación Flask funcionando en Python 3.13!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
    print("Datos recibidos:", data)
    return jsonify({"message": "Alerta recibida correctamente"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
