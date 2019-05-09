from flask import abort, make_response, jsonify

def handle_dialog(client, data):
    channel = data["channel"]["id"]
    poll_options = data.get("submission")
    print(poll_options)
    if not poll_options:
        abort(400)
    options = list(filter(lambda x: x is not None, [
        poll_options.get("poll-option-a"),
        poll_options.get("poll-option-b"),
        poll_options.get("poll-option-c"),
        poll_options.get("poll-option-d"),
    ]))
    if len(options) < 2:
        client.messageEphemeral(channel, data["user"]["id"], "Couldn't create the poll – you need to specify at least two options!")
        return make_response("", 200)
    client.message(channel, create_poll(name["poll-question"], options))
    return make_response("", 200)

handlers = {
    "dialog_submission": handle_dialog
}

def handle_callback(client, data):
    actionType = data.get("type")
    if actionType not in handlers:
        abort(400)
    return handlers[actionType](client, data)

# Dialogs and formatted messages

def create_poll(name, options):
    poll = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*{}*".format(name)
            },
        },
        {
            "type": "divider" 
        }
    ]
    for option in options:
        # Ignore None types
        if not option:
            continue
        poll.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": option,
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "emoji": True,
                    "text": "Vote"
                },
                "value": "vote-btn"
            }
        })
    return poll
