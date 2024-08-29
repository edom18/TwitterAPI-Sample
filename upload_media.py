import os
import hmac
import hashlib
import base64
import requests

# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1

from utility import generate_nonce, get_timestamp, encode_text

import dotenv
dotenv.load_dotenv()

def post(files):

    media_upload_endpoint_url = "https://upload.twitter.com/1.1/media/upload.json"
    oauth_consumer_key = os.environ.get("CONSUMER_KEY")
    oauth_consumer_secret = os.environ.get("CONSUMER_SECRET")
    oauth_nonce = generate_nonce()
    oauth_signature_method = "HMAC-SHA1"
    oauth_timestamp = str(get_timestamp())
    oauth_token = os.environ.get("AUTH_TOKEN")
    oauth_token_secret = os.environ.get("AUTH_TOKEN_SECRET")
    oauth_version = "1.0"

    oauth_parameters = {
        "oauth_consumer_key": oauth_consumer_key,
        "oauth_token": oauth_token,
        "oauth_signature_method": oauth_signature_method,
        "oauth_timestamp": oauth_timestamp,
        "oauth_nonce": oauth_nonce,
        "oauth_version": oauth_version,
    }

    method = "POST"

    # リクエストパラメータ
    all_parameters = oauth_parameters.copy()
    sorted_parameters = "&".join(f"{encode_text(k)}={encode_text(v)}" for k, v in sorted(all_parameters.items()))

    print(f"Sorted Parameters: {sorted_parameters}\n")

    # ベースストリングの作成
    base_string = f"{method}&{encode_text(media_upload_endpoint_url)}&{encode_text(sorted_parameters)}"

    print(f"Base String: {base_string}\n")

    # シグネチャキーの作成
    signing_key = f"{encode_text(oauth_consumer_secret)}&{encode_text(oauth_token_secret)}"

    # シグネチャの生成
    signature = base64.b64encode(hmac.new(signing_key.encode(), base_string.encode(), hashlib.sha1).digest()).decode()

    print(f"Signature: {signature}")

    # Authorization ヘッダーの作成
    oauth_parameters["oauth_signature"] = signature
    auth_header = "OAuth " + ", ".join([f'{encode_text(k)}="{encode_text(v)}"' for k, v in oauth_parameters.items()])

    print(f"Authorization Header: {auth_header}\n")

    # リクエストヘッダーのセット
    headers = {
        "Authorization": auth_header,
    }

    print(f"Access the api [{media_upload_endpoint_url}] ...")

    response = requests.post(media_upload_endpoint_url, headers=headers, files=files)
    return response