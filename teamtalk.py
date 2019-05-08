from flask import Flask
from util import getenv 

# Load constants from .env file
VERIFICATION_TOKEN = getenv("VERIFICATION_TOKEN")
BOT_ACC_TOKEN      = getenv("BOT_ACC_TOKEN")
PORT               = getenv("PORT")

# Pretty print server preamble
print("--------------")
print(f'Running on port {PORT} with:')
print(f'Verification token: {VERIFICATION_TOKEN}')
print(f'Bot User OAuth Access token: {BOT_ACC_TOKEN}')
print("--------------")

# Define the app & routes
app = Flask(__name__)

@app.route("/hello", methods=["POST"])
def hello():
    return "Hello slack!"

# Finally, run the damn thing
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True) 
