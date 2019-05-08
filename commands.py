from flask import abort

def handle_send(text):
    print(text)
    return "Got send: " + text

def handle_poll(text):
    print(text)
    return "Got poll: " + text

handlers = {
    "/send": handle_send,
    "/poll": handle_poll
}

def handle(command, text):
    if command not in handlers:
        abort(400)
    return handlers[command](text)
