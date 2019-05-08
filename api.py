from slackclient import SlackClient

class Client:
    # Create a new client instance
    def __main__(self, bot_access_token):
        self.client = SlackClient(bot_access_token);
    # Send a message to some channel
    def message(self, channel, message):
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
        )
