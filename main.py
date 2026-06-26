from flask import Flask, request, Response, jsonify
import requests
import os

app = Flask(__name__)

PIONEER_API_KEY = os.environ.get("PIONEER_API_KEY", "")
PIONEER_BASE_URL = "https://api.pioneer.ai/v1"

@app.route("/v1/chat/completions", methods=["POST"])
def proxy():
    data = request.get_json()
    h = {
        "Content-Type": "application/json",
        "X-API-Key": PIONEER_API_KEY
    }
    r = requests.post(
        PIONEER_BASE_URL + "/chat/completions",
        json=data,
        headers=h,
        stream=True
    )
    return Response(
        r.iter_content(1024),
        status=r.status_code,
        content_type=r.headers.get("Content-Type")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
