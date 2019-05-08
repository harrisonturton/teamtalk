from flask import abort

def handle_send(client, text):
    params = text.split(" ")
    if len(params) <= 1:
        return "Usage: `/send @user message` or `/send #channel message`"
    user = params[0]
    message = " ".join(params[1:])
    resp = client.messageUser(user, message)
    if resp.status_code != 200:
        return "Failed to send message!"
    return "Sent message: " + message + " to " + user

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
