# LlamaIndex Slack Chatbot
A Simple Slack Bot developed using Python and slack_bolt that interacts with users in a Slack channel, providing responses powered by an external API that utilizes LlamaIndex and AI to process natural language from documents.

## Overview
The bot allows you to chat with an AI assistant powered by any AI provider with documentation injected with LlamaIndex directly within a Slack workspace. It shows how retrival augmented generation can be integrated into an existing chat platform.

### Features
- Responds to events in a defined Slack channel.
- Engages with users through direct messages and @mentions.
- Maintains communication in a thread and avoids responding to its own messages.

## Example
![Alt text](https://github.com/pulsebox/slackChatBot/blob/main/images/ConvoScreenshot%202024-02-17.png)
In the above example I have added my CV into the documents folder, then asked questions about it.

## Usage
Clone this repo
Ensure OPENAI_API_KEY, SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET are in .env file
```bash
pip install -r requirements.txt
python server.py
```

## Contributing
Pull requests are welcome to extend the bot's functionality.

## Possible TODOs

### Interactions
- In case of a 404 error from the API, the bot will notify the user with an error message. 
- In instances of API failure, the bot will wait 1 second and attempt the request again.

### Deployment and Monitoring
- Deployment strategy and hosting platform are under consideration (suggestions welcomed).
- Monitor git pushes and restarts the bot as necessary, primarily during off-hours unless urgent.

### Security
- Implement Prompt Injection prevention to safeguard from potential hijacking.
- Implement a rate limiter to prevent abuse.
