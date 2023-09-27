import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from dotenv import load_dotenv
from functions import draft_email
from fastapi import FastAPI, Request

# Load environment variables from .env file
load_dotenv("token.env")
# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)
# Initialize the FastAPi app
fastapi_app = FastAPI()
# Flask is a web application framework written in Python
handler = SlackRequestHandler(app)

def my_function(text):
    """
    Custom function to process the text and return a response.
    In this example, the function converts the input text to uppercase.

    Args:
        text (str): The input text to process.

    Returns:
        str: The processed text.
    """
    response = text.upper()
    return response

@app.event("app_mention")
def handle_mentions(body, say):
    """
    Event listener for mentions in Slack.
    When the bot is mentioned, this function processes the text and sends a response.

    Args:
        body (dict): The event data received from Slack.
        say (callable): A function for sending a response to the channel.
    """
    text = body["event"]["text"]

    mention = f"<@{SLACK_BOT_USER_ID}>"
    text = text.replace(mention, "").strip()

    say("Sure, I'll get right on that!")
    # response = my_function(text)
    response = draft_email(text)
    say(response)

@fastapi_app.post("/slack/events")
async def slack_events(request: Request):
    """
    Route for handling Slack events.
    This function passes the incoming HTTP request to the SlackRequestHandler for processing.
    Returns:
        Response: The result of handling the request.
    """
    return await handler.handle(request)


# Run the Flask app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)