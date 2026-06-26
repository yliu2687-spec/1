from flask import Flask, request, Response
import requests

app = Flask(__name__)

import os
PIONEER_API_KEY = os.environ.get("PIONEER_API_KEY", "")
PIONEER_BASE_URL = "https://api.pioneer.ai/v1"

@app.route("/messages", methods=["POST"])
def proxy():
    data = request.get_json()
