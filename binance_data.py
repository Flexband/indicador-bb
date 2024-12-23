from flask import Flask, request, jsonify
import requests
import pandas as pd
import json

# Inicializamos Flask
app = Flask(__name__)

# Endpoint que recibiría los datos procesados de Binance
@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()  # Recibimos los datos como JSON
    print("Datos recibidos:", data)

    # Datos que quieres enviar a TradingView
    webhook_url = 'TU_WEBHOOK_URL_DE_TRADINGVIEW'  # Reemplaza esto por la URL del webhook de TradingView
    
    try:
        # Enviar los datos al webhook de TradingView
        response = requests.post(webhook_url, json=data)
        
        # Comprobar si el envío fue exitoso
        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Datos enviados correctamente"}), 200
        else:
            return jsonify({"status": "error", "message": "Error al enviar datos"}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Iniciar el servidor en el puerto 5000
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


















