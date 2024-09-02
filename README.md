# X (Twitter) API + Oauth 1.0a で画像付き投稿をするサンプルプロジェクト

* English version is on below Japanese text.

本プロジェクトは、OAuth 1.0a 認証を利用して X (Twitter) API から画像付きツイートを行うためのデモプロジェクトです。

ライブラリとして利用できるようにするものではなく、あくまでフローを理解するために作ったデモとなります。そのため、一部の処理で手作業でコピペして進めるステップもあります。

# How to use

## 設定ファイルの準備

本リポジトリには `.env-sample` ファイルが含まれています。このサンプルを埋める形でご自身の Consumer Key などを設定してください。設定は `dotenv` を利用して読み込むようになっています。また、ファイルを `.env` にリネームしてください。

## アクセストークンとアクセストークンシークレットの取得

リクエストトークンからアクセストークンを取得するフローは `request-token.py` に実装されています。設定ファイルが適切に設定されていれば、以下のように実行し、手順に従うことでアクセストークンを取得することができます。

```shell:アクセストークンの取得
$ python request-token.py
```

## 画像付きツイート

アクセストークンを取得後、設定ファイルにアクセストークンとアクセストークンシークレットを設定した後、 `main.py` にテキストと画像のファイルパスを渡すことで、画像付き投稿ができます。

```shell:画像付きツイート
$ python main <TEXT> <PATH_TO_IMAGE>
```

本プロジェクトの解説記事を書いているので分からない点などはこちらを参考にしてください。

- [X (Twitter) API + Oauth 1.0a で画像付き投稿をする](https://zenn.dev/edom18/articles/post-media-with-twitter-api)

----------------------------------

# This is a sample project for tweeting with X (Twitter) API with OAuth 1.0a

This project is just a demo project for showing how to use X (Twitter) API with OAuth 1.0a.

This is not aiming to use these APIs as library, just to know authorazing flow.

# How to use

## Prepare the setting file

This repo has `.env-sample` file to let you know how to setup `.env` file. Please fill them out of your information. After fill them out, rename it to `.env` .

## Get an access token and access token secret

You can get these items with `request-token.py` that exchanges a request token and an access token after you filled the setting fiile. Please run a command like below.

```shell:Get an access token
$ python request-token.py
```

## Tweet with a media

If you obtained a user's access token, please fill the setting file out with the tocken then run a command like below.

```shell:Tweet a message with a media
$ python main <TEXT> <PATH_TO_IMAGE>
```