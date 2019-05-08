from flask import Flask, request, jsonify, abort
from util import getenv 
from api import Client

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

def handle_send(text):
    print(text)
    return "Got send: " + text

def handle_poll(text):
    print(text)
    return "Got poll: " + text

command_handlers = {
    "/send": handle_send,
    "/poll": handle_poll
}

@app.route("/commands", methods=["POST"])
def commands():
    print(request.form)
    # Validate the token
    token = request.form.get("token", None)
    if token != VERIFICATION_TOKEN:
        abort(401)
    # Parse command and delegate to handler
    command = request.form.get("command", None)
    text = request.form.get("text", None)
    print(command)
    if command not in command_handlers:
        abort(400)
    return command_handlers[command](text)

# Finally, run the damn thing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True) 
