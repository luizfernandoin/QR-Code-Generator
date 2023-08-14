from app import app
from flask import render_template, url_for, jsonify, request
from main import gerar

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/generator", methods=["POST"])
def generator():
    data = request.json
    textInput = data.get("textInput")
    try:
        arquivo = gerar(textInput)
        # Se gerar() não gerar erros, então o QR code foi gerado com sucesso
        return jsonify({"status": "qrcode_generated", "arquivo": arquivo})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
