import os
from pathlib import Path

from flask import Flask, abort, jsonify, send_from_directory

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/<name>.csv")
def csv_file(name):
    # Only serve the two CSV files the dashboard reads
    if name not in ("input", "cleaned_output"):
        abort(404)
    return send_from_directory(BASE_DIR, f"{name}.csv", mimetype="text/csv", max_age=0)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
