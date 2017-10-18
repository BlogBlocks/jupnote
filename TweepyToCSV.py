import sys
import tweepy
import csv
import Key

#pass security information to variables
consumer_key = Key.twiter()[0]
consumer_secret = Key.twiter()[1]
access_key = Key.twiter()[2]
access_secret = Key.twiter()[3]

#use variables to access twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#create an object called 'customStreamListener'
class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print (status.author.screen_name, status.created_at, status.text)
        # Writing status data
        with open('OutputStreaming.txt', 'a') as f:
            writer = csv.writer(f)
            #status.author.screen_name = status.author.screen_name.encode('UTF-8')
            #status.text.encode = status.text.encode('UTF-8')            
            writer.writerow([status.author.screen_name.encode('UTF-8'), status.created_at, status.text.encode('utf8')])


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


    def titles():
        # Writing csv titles
        with open('OutputStreaming.txt', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Author', 'Date', 'Text'])
            
def main():
    streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
    #with open("tokens.txt", "r") as f:
    with open("tokens2.txt", "r") as f:    
        tokens = f.readlines()

        streamingAPI.filter(track=tokens)
        #streamingAPI.filter(track=['Dallas', 'NewYork'])


        #status.text.encode('utf-8')
        #writer.writerow([unicode(s).encode("utf-8") for s in row])
        #writer.writerow([unicode('Author', 'Date', 'Text').encode("utf-8") for 'Author', 'Date', 'Text' in row])