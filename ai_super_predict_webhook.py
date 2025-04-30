
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/webhook/ai-predict', methods=['GET'])
def get_prediction():
    return jsonify({
        "symbol": "LOOKSUSDT",
        "timeframe": "5m",
        "direction": "long",
        "confidence": 83.5,
        "delta": 3.2
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
