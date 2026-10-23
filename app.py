
from pathlib import Path
from flask import Flask, jsonify, send_from_directory
import os

# Project directory
BASE_DIR = Path(__file__).resolve().parent
DASHBOARD_FILE = BASE_DIR / "index.html"

# Flask application
app = Flask(__name__)

@app.route("/")
def home():
    """Serve the SkyRoute Logistics dashboard."""
    if DASHBOARD_FILE.exists():
        return send_from_directory(str(BASE_DIR), "index.html")

    return (
        "SkyRoute dashboard file not found. "
        "Please ensure index.html is included in the repository."
    ), 404


@app.route("/health")
def health():
    """Health check endpoint for deployment monitoring."""
    return jsonify({
        "status": "healthy",
        "application": "SkyRoute Logistics Data Pipeline"
    }), 200


@app.route("/favicon.ico")
def favicon():
    """Avoid a missing favicon error in browser requests."""
    return "", 204


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
