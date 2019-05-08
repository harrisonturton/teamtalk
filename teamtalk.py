from flask import Flask
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
slack_client = SlackClient(VERIFICATION_TOKEN)

@app.route("/send", methods=["POST"])
def hello(data):
    print(data)
    slack_client.api_call(
        "chat.postMessage",
        channel="general",
        text="Hello from Python!" 
    )

# Finally, run the damn thing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True) 
