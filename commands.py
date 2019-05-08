from flask import abort

def handle_send(client, text):
    print(text)
    client.messageUser("@harrisonturton", "Hello harry")
    return "Got send: " + text

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
