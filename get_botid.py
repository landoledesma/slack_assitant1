import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv


load_dotenv("token.env")

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
def get_bot_user_id():
    """
    Get the bot user ID using the Slack API.
    Returns:
        str: The bot user ID.
    """
    try:
        # Initialize the Slack client with your bot token
        slack_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        response = slack_client.auth_test()
        return response["user_id"]
    except SlackApiError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    bot_user_id = get_bot_user_id()
    print(f"Bot User ID: {bot_user_id}")
