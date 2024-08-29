import os
import requests

from utility import create_oauth_header

import dotenv
dotenv.load_dotenv()

def post(files):

    endpoint_url = "https://upload.twitter.com/1.1/media/upload.json"

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
        verbose=False)

    # リクエストヘッダーのセット
    headers = {
        "Authorization": auth_header,
    }

    print(f"Access the api [{endpoint_url}] ...")

    response = requests.post(endpoint_url, headers=headers, files=files)
    return response