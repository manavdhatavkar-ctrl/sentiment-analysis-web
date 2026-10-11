from flask import Flask, jsonify, request

from src.sentiment import analyze_sentiment

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Sentiment Analysis API!",
        "usage": {
            "method": "POST",
            "endpoint": "/analyze",
            "content_type": "application/json",
            "body": {
                "text": "I love this product!"
            }
        }
    })


@app.route("/analyze", methods=["POST"])
def analyze():
    if not request.is_json:
        return jsonify({
            "error": "Request must contain JSON data."
        }), 415

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a JSON object."
        }), 400

    text = data.get("text")

    if not isinstance(text, str) or not text.strip():
        return jsonify({
            "error": "Please provide non-empty text."
        }), 400

    result = analyze_sentiment(text)

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
