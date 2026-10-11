
from flask import Flask, jsonify, render_template, request

from src.sentiment import analyze_sentiment

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
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

        return jsonify(analyze_sentiment(text)), 200

    if request.is_json is False and request.mimetype != "application/x-www-form-urlencoded":
        return jsonify({
            "error": "Unsupported request content type."
        }), 415

    text = request.form.get("text", "")

    if not text.strip():
        return "Please enter some text before analyzing.", 400

    result = analyze_sentiment(text)

    return render_template(
        "result.html",
        text=text,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
