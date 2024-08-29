import os
import requests

from utility import create_oauth_header

import dotenv
dotenv.load_dotenv()

oauth_consumer_key = os.environ.get("CONSUMER_KEY")
oauth_consumer_secret = os.environ.get("CONSUMER_SECRET")
oauth_token = os.environ.get("AUTH_TOKEN")
oauth_token_secret = os.environ.get("AUTH_TOKEN_SECRET")

callback_url = "https://hippogames.dev/api/oauth/redirect"
request_endpoint_url = "https://api.twitter.com/oauth/request_token"
authenticate_url = "https://api.twitter.com/oauth/authenticate"

auth_header = create_oauth_header(
    endpoint_url=request_endpoint_url,
    oauth_consumer_key=oauth_consumer_key,
    oauth_consumer_secret=oauth_consumer_secret,
    oauth_token=oauth_token,
    oauth_token_secret=oauth_token_secret,
    verbose=False)

req_headers = {
    "Authorization": auth_header,
}

request_token_params = {
    "oauth_callback": callback_url,
}
response_req = requests.post(request_endpoint_url, headers=req_headers, json=request_token_params)
response_req_text = response_req.text

oauth_token_kvstr = response_req_text.split("&")
token_dict = {x.split("=")[0]: x.split("=")[1] for x in oauth_token_kvstr}
req_oauth_token = token_dict["oauth_token"]

print("Please access the following URL and get the OAuth Verifier.")
print(f"{authenticate_url}?oauth_token={req_oauth_token}")

oauth_verifier = input("OAuth Verifierを入力してください> ")

access_endpoint_url = "https://api.twitter.com/oauth/access_token"

auth_header = create_oauth_header(
    endpoint_url=access_endpoint_url,
    oauth_consumer_key=oauth_consumer_key,
    oauth_consumer_secret=oauth_consumer_secret,
    oauth_token=req_oauth_token,
    oauth_token_secret=oauth_token_secret,
    oauth_verifier=oauth_verifier,
    verbose=False)

acc_headers = {
    "Authorization": auth_header,
}

verifier_params = {
    "oauth_token": req_oauth_token,
    "oauth_verifier": oauth_verifier,
}
response_acc = requests.post(access_endpoint_url, headers=acc_headers, json=verifier_params)
response_acc_text = response_acc.text
print(response_acc_text)