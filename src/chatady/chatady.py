import requests
import json

class ChatADy:
    def __init__(self, publisher_id, key, options=None):
        if options is None:
            options = {}
        self.publisher_id = publisher_id
        self.key = key
        self.options = {'environment': 'production', 'noDelay': True, 'timeout': 1000}
        self.options.update(options)
        self.hostname = 'backend.chatady.com'
        self.port = 443
        self.prepath = '/api/v1'

    def new_chat(self, chat_id, chatter_id, entry, ad=None):
        post_data = json.dumps({'entry': entry, 'ad': ad})
        path = f"{self.prepath}/{'chats' if self.options['environment'] == 'production' else 'test-chats'}/{self.publisher_id}/{chat_id}/{chatter_id}"
        url = f"https://{self.hostname}:{self.port}{path}"
        headers = {
            'Content-Type': 'application/json',
            'Content-Length': str(len(post_data)),
            'Authorization': self.key
        }
        response = requests.post(url, headers=headers, data=post_data, timeout=self.options['timeout'])
        return response.text