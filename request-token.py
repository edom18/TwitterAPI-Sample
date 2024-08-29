import os

from requests_oauthlib import OAuth1Session

import dotenv
dotenv.load_dotenv()

API_KEY = os.environ.get("CONSUMER_KEY")
API_KEY_SECRET = os.environ.get("CONSUMER_SECRET")

callback_url = "https://hippogames.dev/api/oauth/redirect"
request_endpoint_url = "https://api.twitter.com/oauth/request_token"
authenticate_url = "https://api.twitter.com/oauth/authenticate"

session_req = OAuth1Session(API_KEY, API_KEY_SECRET)
response_req = session_req.post(request_endpoint_url, params={"oauth_callback": callback_url})
response_req_text = response_req.text

oauth_token_kvstr = response_req_text.split("&")
token_dict = {x.split("=")[0]: x.split("=")[1] for x in oauth_token_kvstr}
oauth_token = token_dict["oauth_token"]

print("Please access the following URL and get the OAuth Verifier.")
print(f"{authenticate_url}?oauth_token={oauth_token}")

oauth_verifier = input("OAuth Verifierを入力してください> ")

access_endpoint_url = "https://api.twitter.com/oauth/access_token"

session_acc = OAuth1Session(API_KEY, API_KEY_SECRET, oauth_token, oauth_verifier)
response_acc = session_acc.post(access_endpoint_url, params={"oauth_verifier": oauth_verifier})
response_acc_text = response_acc.text

print(response_acc_text)