from slackclient import SlackClient

class Client:
    # Create a new client instance
    def __init__(self, bot_access_token):
        self.client = SlackClient(bot_access_token);
    # Send a message to some channel or user. The users ID
    # is used in place of the channel ID.
    def message(self, channel, message):
        return self.client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
        )
    def messageBlocks(self, channel, blocks):
        return self.client.api_call(
            "chat.postMessage",
            channel=channel,
            blocks=blocks
        )
    def messageEphemeral(self, channel, user, message):
        return self.client.api_call(
            "chat.postEphemeral",
            channel=channel,
            text=message,
            user=user
        )
    def updateMessage(self, channel, timestamp, message):
        return self.client.api_call(
            "chat.update",
            channel=channel,
            ts=timestamp,
            message=message
        )
    # Open a dialog
    def openDialog(self, trigger_id, dialog):
        return self.client.api_call(
            "dialog.open",
            trigger_id=trigger_id,
            dialog=dialog
        )
