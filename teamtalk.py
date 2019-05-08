from flask import Flask, request, jsonify, abort, make_response
from util import getenv 
from client import Client
from commands import handle
import json

# Load constants from .env file
VERIFICATION_TOKEN = getenv("VERIFICATION_TOKEN")
BOT_ACC_TOKEN      = getenv("BOT_ACC_TOKEN")
PORT               = getenv("PORT")

# Pretty print server preamble
print("--------------")
print("Running on port", PORT, "with:")
print("Verification token:", VERIFICATION_TOKEN)
print("Bot User OAuth Access token:", BOT_ACC_TOKEN)
print("--------------")

# Define the app & routes
app = Flask(__name__)
client = Client(BOT_ACC_TOKEN)

# Handles slash commands
@app.route("/commands", methods=["POST"])
def commands():
    # print(request.form)
    # Validate the token
    token = request.form.get("token")
    if token != VERIFICATION_TOKEN:
        abort(401)
    # Delegate command to handlers
    return handle(client, request)

# Handles dialog submissions, button clicks, etc
@app.route("/callbacks", methods=["POST"])
def callbacks():
    payload = request.form.get("payload")
    if not payload:
        abort(500)
    data = json.loads(payload)
    print(data)
    # Validate token
    token = data.get("token")
    if token != VERIFICATION_TOKEN:
        abort(401)
    if data.get("type") == "dialog_submission":
        print("Handling dialog submission")
    return make_response("", 200)


# Finally, run the damn thing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True) 
