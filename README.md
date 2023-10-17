# Cleverbot-Free

Cleverbot-Free is a Python library that allows you to interact with the Cleverbot API and have conversations with Cleverbot, an AI chatbot.

## Installation

You can install Cleverbot-Free using pip:

bash
pip install cleverbot-free
## Usage
To use this code, you can call the `send_message()` function with the stimulus (message) you want to send to Cleverbot and optionally provide a context and language.

Here's an example of how you can use this code:

from cleverbot-free import send_message

response = send_message("Hello, how are you?")
print("Cleverbot:", response)

This will send the message "Hello, how are you?" to Cleverbot and print its response.

Please note that this code relies on the Cleverbot API and may not always provide the same quality of responses as the official Cleverbot API. Also, keep in mind that the code is not officially supported by Cleverbot and may break if the API changes.

## Api 
Cleverbot-Free does not require an API key to use the Cleverbot API. It uses a simplified version of the Cleverbot protocol, which does not require authentication.
