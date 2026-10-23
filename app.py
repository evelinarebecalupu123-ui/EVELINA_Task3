
from flask import Flask, jsonify
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SkyRoute Logistics Data Pipeline</h1>
    <p>Application is running successfully.</p>
    <p>Python data pipeline project deployed on Render.</p>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
