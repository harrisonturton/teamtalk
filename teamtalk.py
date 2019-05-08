from flask import Flask, request, jsonify, abort
from util import getenv 
from client import Client
from commands import handle

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

@app.route("/commands", methods=["POST"])
def commands():
    print(request.form)
    # Validate the token
    token = request.form.get("token", None)
    if token != VERIFICATION_TOKEN:
        abort(401)
    # Delegate command to handlers
    return handle(client, request)

# Finally, run the damn thing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True) 
