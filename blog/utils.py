import tweepy
import bitly_api
from django.conf import settings

def smart_truncate(content, length=64, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

def tweet(title, uri):
    bitly = bitly_api.Connection(settings.BITLY_USER, settings.BITLY_KEY) 
    short_url = bitly.shorten(uri)
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    title = smart_truncate(title) + ' -- '
    post_update = title + short_url['url']
    status = api.update_status(post_update)
    return status
