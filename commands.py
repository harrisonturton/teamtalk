from flask import abort, jsonify

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
    resp = client.openDialog(trigger_id, {
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
                "optional": False
            },
            {
                "type": "text",
                "label": "Option B",
                "name": "poll-option-b",
                "optional": False
            },
            {
                "type": "text",
                "label": "Option C",
                "name": "poll-option-c",
                "optional": False
            },
            {
                "type": "text",
                "label": "Option D",
                "name": "poll-option-d",
                "optional": False
            }
        ]
    })
    if not resp.get("ok"):
        print(resp)
        return "Failed to create poll."
    return "Created poll!"

# Map the user-facing slash command to the
# relevant handler.
handlers = {
    "/send": handle_send,
    "/poll": handle_poll
}

def handle(client, request):
    command = request.form.get("command", None)
    text = request.form.get("text", None)
    trigger_id = request.form.get("trigger_id", None)
    if command not in handlers:
        abort(400)
    return handlers[command](client, text, trigger_id)
