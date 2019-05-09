from flask import abort, jsonify, make_response

def handle_send(client, text, trigger_id):
    params = text.split(" ")
    if len(params) <= 1:
        return "Sorry! I didn't understand that.\n> Usage: `/send @user message` or `/send #channel message`"
    destination = params[0]
    message = " ".join(params[1:])
    resp = client.message(destination, "*You received an anonymous message*\n> {}".format(message))
    if not resp.get("ok"):
        return "_Failed to send message {} to {}_. Did you make a typo?".format(message, destination),
    return "Sent message: {} to {}".format(message, destination)

def handle_poll(client, text, trigger_id):
    resp = client.openDialog(trigger_id, create_poll_dialog())
    if not resp.get("ok"):
        print(resp)
        return "Failed to create poll."
    return make_response("", 200)

# Map the user-facing slash command to the
# relevant handler.
handlers = {
    "/send": handle_send,
    "/poll": handle_poll
}

def handle_command(client, request):
    command = request.form.get("command")
    text = request.form.get("text")
    trigger_id = request.form.get("trigger_id")
    if command not in handlers:
        abort(400)
    return handlers[command](client, text, trigger_id)

# Dialogs and formatted messages

def create_poll_dialog():
    return {
        "title": "Create New Poll",
        "submit_label": "Create",
        "callback_id": "new-poll",
        "elements": [
            {
                "type": "text",
                "label": "Poll Question",
                "name": "poll-question",
                "optional": False
            },
            {
                "type": "text",
                "label": "Option A",
                "name": "poll-option-a",
                "optional": True
            },
            {
                "type": "text",
                "label": "Option B",
                "name": "poll-option-b",
                "optional": True
            },
            {
                "type": "text",
                "label": "Option C",
                "name": "poll-option-c",
                "optional": True
            },
            {
                "type": "text",
                "label": "Option D",
                "name": "poll-option-d",
                "optional": True
            }
        ]
    }
