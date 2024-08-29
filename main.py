import sys

from upload_media import post as upload_media_post
from post_tweet import request as post_tweet_request

def main(tweet_text, image_file_path):

    file = open(image_file_path, "rb")
    files = {
        "media": file,
    }

    response = upload_media_post(files)

    # レスポンスの確認
    if response.status_code == 200:
        print("Tweet posted successfully!")
    else:
        print(f"Failed to post tweet. Status code: {response.status_code}")
        print(response.json())

    # --------------------------------

    media_id = response.json()["media_id_string"]

    parameters = {
        "text": tweet_text,
        "media": {
            "media_ids": [media_id],
        },
    }

    tweet_response = post_tweet_request(parameters)

    # レスポンスの確認
    if tweet_response.status_code == 201:
        print("Tweet posted successfully!")
    else:
        print(f"Failed to post tweet. Status code: {tweet_response.status_code}")
        print(response.json())

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python main.py [tweet text] [image file path]")
        sys.exit(1)

    tweet_text = sys.argv[1]
    image_file_path = sys.argv[2]
    main(tweet_text, image_file_path)