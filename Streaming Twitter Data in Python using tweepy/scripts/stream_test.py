#author : Yuwono Bangun Nagoro (a.k.a SurgicalSteel)

from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import tweepy
import sys
auth = tweepy.OAuthHandler("YOUR-CONSUMER-KEY","YOUR-CONSUMER-SECRET")
auth.set_access_token("YOUR-ACCESS-TOKEN","YOUR-TOKEN-SECRET")
api = tweepy.API(auth)

class mylistener(StreamListener):
    i=1
    def on_data(self,data):
        mydata=json.loads(data) #as known before that 'data' is a string type variable, so I can just perform json.loads
        print (str(self.i)+". "+mydata['user']['name']+" (@"+mydata['user']['screen_name']+") : "+mydata['text'])
        #print(data)
        self.i+=1
        return True
    def on_error(self,status):
        print(status)

if __name__=='__main__':
    inp=sys.stdin.readline()
    listen=mylistener()
    stream=Stream(auth,listen)
    stream.filter(track=[inp]) #use a single variable as keyword
