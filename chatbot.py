systemPrompt = "You are a helpful and useful Slack chat bot, be very concise"

config = {
    "openai": {
      "model": "gpt-3.5-turbo",
      "temperature": 0.7,
      "max_tokens": 1024
    },
    "system_prompt": systemPrompt
}

def chatbot_message_response(message, client):

    formatted_messages = []

    # Add the user's message to the formatted_messages list
    formatted_messages.append({"role": "system", "content": config["system_prompt"]})

    formatted_messages.append({"role": "user", "content": message['text']})

    # Get the response from the OpenAI API
    completion = client.chat.completions.create(
        messages = formatted_messages,
        model="gpt-3.5-turbo",
    )
    # Get the bot's response
    botResponse = completion.choices[0].message.content
    # Return the bot's response
    return botResponse
