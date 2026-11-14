
from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Azure Flask Demo</title>
        </head>
        <body style="text-align:center; font-family:Arial;">
            <h1>Welcome to Azure App Service!</h1>
            <h2>Python Flask Application</h2>
            <p>Your application is successfully deployed.</p>
            <p>Environment: Azure</p>
            <a href="/health">Check Application Health</a>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "application": "Flask Azure Demo",
        "environment": os.getenv("WEBSITE_SITE_NAME", "Local"),
        "timestamp": datetime.utcnow().isoformat()
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
