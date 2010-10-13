import tweepy
import bitly_api
from django.conf import settings

def tweet(title, uri):
    bitly = bitly_api.Connection(settings.BITLY_USER, settings.BITLY_KEY) 
    short_url = bitly.shorten(uri)
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    title = title + ' -- '
    post_update = title + short_url['url']
    status = api.update_status(post_update)
    return status
