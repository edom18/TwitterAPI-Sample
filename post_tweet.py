import os
import requests

from utility import create_oauth_header

import dotenv
dotenv.load_dotenv()

def request(parameters):

    endpoint_url = "https://api.twitter.com/2/tweets"

    oauth_consumer_key = os.environ.get("CONSUMER_KEY")
    oauth_consumer_secret = os.environ.get("CONSUMER_SECRET")
    oauth_token = os.environ.get("AUTH_TOKEN")
    oauth_token_secret = os.environ.get("AUTH_TOKEN_SECRET")

    auth_header = create_oauth_header(
        endpoint_url=endpoint_url,
        oauth_consumer_key=oauth_consumer_key,
        oauth_consumer_secret=oauth_consumer_secret,
        oauth_token=oauth_token,
        oauth_token_secret=oauth_token_secret,
        verbose=True)

    # リクエストヘッダーのセット
    headers = {
        "Content-Type": "application/json",
        "Authorization": auth_header,
    }

    print(f"Access the api [{endpoint_url}] ...")

    response = requests.post(endpoint_url, headers=headers, json=parameters)
    return response

if __name__ == "__main__":
    parameters = {
        "text": "Hello, Twitter API!",
    }
    response = request(parameters)
    print(response.text)