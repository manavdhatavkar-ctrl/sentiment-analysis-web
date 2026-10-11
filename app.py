
from flask import Flask, jsonify, render_template, request

from src.sentiment import analyze_sentiment

app = Flask(__name__)

MAX_TEXT_LENGTH = 5000


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Handle JSON API requests
    if request.is_json:
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

        if len(text) > MAX_TEXT_LENGTH:
            return jsonify({
                "error": "Text must not exceed 5,000 characters."
            }), 400

        result = analyze_sentiment(text)

        return jsonify(result), 200

    # Handle HTML form submissions
    if request.mimetype != "application/x-www-form-urlencoded":
        return jsonify({
            "error": "Unsupported request content type."
        }), 415

    text = request.form.get("text", "")

    if not text.strip():
        return "Please enter some text before analyzing.", 400

    if len(text) > MAX_TEXT_LENGTH:
        return "Text must not exceed 5,000 characters.", 400

    result = analyze_sentiment(text)

    return render_template(
        "result.html",
        text=text,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
