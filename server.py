import os
from pathlib import Path
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

import logging as logger

# Load the .env file to get the token
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Set up logging
logger.basicConfig(level=logger.DEBUG)

# Initialize the Slack Bolt app
# Assume that SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET are in .env
app = App(
    token=os.environ.get("SLACK_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listen for all messages in channels the bot is a member of
@app.message()
def handle_message(message, say):
    logger.debug(message)
    say("What's up?")

# Respond to messages that mention the bot


# Initialize Flask app
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# All requests to the /slack/events endpoint will go through the SlackRequestHandler
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# Start the Flask app
if __name__ == "__main__":
    flask_app.run(port=int(os.environ.get("PORT", 3000))) 