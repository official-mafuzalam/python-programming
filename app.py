import string
import random
from flask import Flask, redirect, request

app = Flask(__name__)

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://localhost:5000/"
        self.key_length = 6
        self.chars = string.ascii_letters + string.digits

    def generate_key(self):
        """Generate a unique key for the short URL."""
        while True:
            key = ''.join(random.choice(self.chars) for _ in range(self.key_length))
            if key not in self.url_mapping:
                return key

    def shorten_url(self, long_url):
        """Shorten the given URL."""
        key = self.generate_key()
        self.url_mapping[key] = long_url
        return self.base_url + key

    def retrieve_url(self, short_url):
        """Retrieve the original URL from the shortened version."""
        key = short_url.replace(self.base_url, "")
        return self.url_mapping.get(key, None)

# Create an instance of the URLShortener
shortener = URLShortener()

@app.route('/shorten', methods=['POST'])
def shorten():
    """Shorten a URL."""
    data = request.json
    long_url = data.get('url')
    if long_url:
        short_url = shortener.shorten_url(long_url)
        return {'short_url': short_url}
    else:
        return {'error': 'URL not provided'}, 400

@app.route('/<key>')
def redirect_to_original_url(key):
    """Redirect to the original URL."""
    original_url = shortener.retrieve_url(shortener.base_url + key)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
