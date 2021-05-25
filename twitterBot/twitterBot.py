import os
import tweepy
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
dotenv_path = BASE_DIR + '/../../.env'
load_dotenv(dotenv_path)


def twitter_bot():
    auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_KEY_SECRET"))
    auth.set_access_token(os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth)
    message = "Hello Test Message from my Twitter Bot"
    api.update_status(message)


twitter_bot()

