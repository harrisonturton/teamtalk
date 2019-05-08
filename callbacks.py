from flask import abort, make_response, jsonify

def handle_dialog(client, data):
    poll_options = data.get("submission")
    if not poll_options:
        abort(400)
    options = filter([
        poll_options.get("poll-option-a"),
        poll_options.get("poll-option-b"),
        poll_options.get("poll-option-c"),
        poll_options.get("poll-option-d")
    ], lambda x: x is not None)
    if len(options) < 2:
        return make_response("Must specify at least 2 options", 200)
    return jsonify({
        [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": poll_options["poll-question"]
                }
            }
        ] 
    })
    return make_response("", 200)

handlers = {
    "dialog_submission": handle_dialog
}

def handle_callback(client, data):
    actionType = request.form.get("type")
    if actionType not in handlers:
        abort(400)
    return handlers[actionType](client, data)
