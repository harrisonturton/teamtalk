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
