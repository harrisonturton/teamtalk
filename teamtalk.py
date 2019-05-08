from flask import Flask, request, jsonify, abort
from util import getenv 
from slackclient import SlackClient

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
slack_client = SlackClient(BOT_ACC_TOKEN)

@app.route("/send", methods=["POST"])
def hello():
    print(request.form)
    token = request.form.get("token", None)
    command = request.form.get("command", None)
    text = request.form.get("text", None)
    channel_id = request.form.get("channel_id", None)
    if not token:
        abort(400)
    if channel_id:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel_id,
            text="Sent a message! :tada:" 
        )
    return "Hello from Teamtalk!"

# Finally, run the damn thing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True) 
