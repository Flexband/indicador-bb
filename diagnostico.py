from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        print("=== INICIO DIAGNÓSTICO ===")

        # Imprimir todo lo que recibe Flask
        print("1. Datos crudos recibidos (request.data):", request.data)
        print("2. Content-Type recibido (request.content_type):", request.content_type)
        print("3. Headers recibidos (request.headers):", dict(request.headers))

        # Intentar extraer JSON
        payload = request.get_json(silent=True)
        print("4. Payload recibido (JSON):", payload)

        # Validar si el payload es válido
        if not payload:
            print("ERROR: JSON vacío o inválido")
            return jsonify({"error": "Invalid JSON"}), 400

        # Extraer información del payload
        symbol = payload.get("symbol", None)
        interval = payload.get("interval", None)
        print("5. Símbolo recibido:", symbol)
        print("6. Intervalo recibido:", interval)

        if not symbol or not interval:
            print("ERROR: Falta 'symbol' o 'interval'")
            return jsonify({"error": "Missing symbol or interval"}), 400

        # Responder con éxito
        print("=== FIN DIAGNÓSTICO ===")
        return jsonify({"message": "Datos procesados correctamente", "data": payload})

    except Exception as e:
        print("ERROR INESPERADO:", str(e))
        return jsonify({"error": "Unexpected error", "detail": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



