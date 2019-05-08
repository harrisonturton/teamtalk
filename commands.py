from flask import abort, jsonify

def handle_send(client, text):
    params = text.split(" ")
    if len(params) <= 1:
        return "Sorry! I don't understand that.\nUsage: `/send @user message` or `/send #channel message`"
    destination = params[0]
    message = " ".join(params[1:])
    resp = client.message(destination, "*Anonymous Message*:\n{}".format(message))
    if not resp.get("ok"):
        return "_Failed to send message {} to {}_. Did you make a typo?".format(message, destination),
    return "Sent message: {} to {}".format(message, destination)

def handle_poll(client, text):
    print(text)
    return "Got poll: " + text

# Map the user-facing slash command to the
# relevant handler.
handlers = {
    "/send": handle_send,
    "/poll": handle_poll
}

def handle(client, command, text):
    if command not in handlers:
        abort(400)
    return handlers[command](client, text)
