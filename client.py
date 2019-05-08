from slackclient import SlackClient

class Client:
    # Create a new client instance
    def __init__(self, bot_access_token):
        self.client = SlackClient(bot_access_token);
    # Send a message to some channel
    def messageChannel(self, channel, message):
        return self.client.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
        )
    def messageUser(self, user, message):
        return self.client.api_call(
            "chat.postMessage",
            channel=user,
            text=message
        )
