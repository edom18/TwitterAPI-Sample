import os
from requests_oauthlib import OAuth1Session

import dotenv
dotenv.load_dotenv()

# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1

# APIキーとトークン
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("AUTH_TOKEN")
access_token_secret = os.environ.get("AUTH_TOKEN_SECRET")

# OAuth1セッションの作成
twitter = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret
)

# ツイート投稿用のエンドポイント
url = "https://api.twitter.com/2/tweets"

# 投稿するツイートの内容
payload = {
    "text": "Hello, Twitter API v2!",
    "media": {
        "media_ids": ["1829075979844874240"],
    },
}

# リクエストの送信
response = twitter.post(url, json=payload)

# レスポンスの確認
if response.status_code == 201:
    print("ツイートが成功しました！")
    print(response.json())
else:
    print(f"エラーが発生しました: {response.status_code}")
    print(response.text)