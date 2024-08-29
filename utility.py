import time
import datetime
import urllib.parse
import random
import string

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