import time
import datetime
import urllib.parse
import random
import string
import base64
import hmac
import hashlib

def generate_nonce(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_timestamp():
    # 現在の時刻をUTCで取得
    now = datetime.datetime.utcnow()

    # UNIXタイムスタンプを取得（秒単位）
    timestamp = int(time.mktime(now.timetuple()))

    return timestamp

def encode_text(text):
    # RFC 3986 に基づく URL エンコード
    return urllib.parse.quote(text, safe='')

def create_oauth_header(
        endpoint_url,
        oauth_consumer_key,
        oauth_consumer_secret,
        oauth_token,
        oauth_token_secret,
        verbose=False,
        **additional_parameters):

    method = "POST"
    oauth_nonce = generate_nonce()
    oauth_timestamp = str(get_timestamp())
    oauth_signature_method = "HMAC-SHA1"
    oauth_version = "1.0"

    oauth_parameters = {
        "oauth_consumer_key": oauth_consumer_key,
        "oauth_token": oauth_token,
        "oauth_signature_method": oauth_signature_method,
        "oauth_timestamp": oauth_timestamp,
        "oauth_nonce": oauth_nonce,
        "oauth_version": oauth_version,
    }

    # Create a sorted parameters
    all_parameters = oauth_parameters.copy()
    all_parameters.update(additional_parameters)
    sorted_parameters = "&".join(f"{encode_text(k)}={encode_text(v)}" for k, v in sorted(all_parameters.items()))

    # ベースストリングの作成
    base_string = f"{method}&{encode_text(endpoint_url)}&{encode_text(sorted_parameters)}"

    # Create a signing key
    signing_key = f"{encode_text(oauth_consumer_secret)}&{encode_text(oauth_token_secret)}"

    # Create a signature
    signature = base64.b64encode(hmac.new(signing_key.encode(), base_string.encode(), hashlib.sha1).digest()).decode()

    if verbose:
        print(f"Base String: {base_string}")
        print("---------------------------------------------")
        print(f"Signing Key: {signing_key}")
        print("---------------------------------------------")
        print(f"Sorted Parameters: {sorted_parameters}")
        print("---------------------------------------------")
        print(f"Base String: {base_string}")
        print("---------------------------------------------")
        print(f"Signature: {signature}")

    # Authorization ヘッダーの作成
    all_parameters["oauth_signature"] = signature
    auth_header = "OAuth " + ", ".join([f'{encode_text(k)}="{encode_text(v)}"' for k, v in all_parameters.items()])

    return auth_header