# ChatADy Package for Python

The `ChatADy` package is a Python wrapper for the ChatADy API, facilitating easy interaction with ChatADy's services from Python applications. It offers methods to send in messages and retrieve AD content.

## Installation

To install ChatADy, run this command in your terminal:

```bash
pip install chatady
```

This is the preferred method to install ChatADy, as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

## Usage

To use the `ChatADy` package, you first need to import the `ChatADy` class from the package and then initialize it with your publisher ID and key.

### Quick Start

Here's a quick example to get you started:

```python
from chatady.chatady import ChatADy

# Initialize the ChatADy client
client = ChatADy('your_publisher_id', 'your_api_key')

# Send in messages
response = client.new_chat('unique_id_conversation', 'unique_id_speaker', 'speaker_message', 'request_ad_type')
print(response)


### Initializing the Client

To interact with the API, you need to create an instance of `ChatADy`:

```python
client = ChatADy('your_publisher_id', 'your_api_key')
```

You can also pass additional options as a dictionary to configure the client further:

```python
options = {'environment': 'production', 'noDelay': True, 'timeout': 1000}
client = ChatADy('your_publisher_id', 'your_api_key', options)
```

### Sending in a new chat message

To start a new chat, use the `new_chat` method with the chat ID, speaker ID and speaker message:

```python
response = client.new_chat('conversation_id_1', 'speaker_id_1', 'Hello, ChatADy!')
print(response)
```

### Sending in a new chat message & retrieve AD content

To start a new chat, use the `new_chat` method with the chat ID, speaker ID and speaker message:

```python
response = client.new_chat('conversation_id_1', 'speaker_id_1', 'Hello, ChatADy!', 'PPC-TEXTLINK')
print(response)
```

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
