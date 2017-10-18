# post image and tweet to Twitter
# USAGE: import Tpost
# Tpost.tpost(ImgPath,STR)
import sys
import twython
from twython import Twython
import Key
def tpost(ImgPath,STR):
    CONSUMER_KEY = Key.twiter()[0]
    CONSUMER_SECRET = Key.twiter()[1]
    ACCESS_KEY = Key.twiter()[2]
    ACCESS_SECRET = Key.twiter()[3]
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,ACCESS_SECRET)
    photo = open(ImgPath,'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=STR, media_ids=[response['media_id']])