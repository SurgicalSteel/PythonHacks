#author : Yuwono Bangun Nagoro (a.k.a SurgicalSteel)

from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import tweepy
import sys
auth = tweepy.OAuthHandler("8FFhYU4Uf2uNxqB2PWDCkOF3y","za03dIX7yR1L9ZBzTVDbnBzK4A3tA7EJzmyY909vgAeVbg8cGB")
auth.set_access_token("206679796-MWUsxrgOU0K6USKX5AvC12J0GlwZ9lRVxO3VD67m","IPg2fOqq0u558isQn9WYYuOGxORimf76hWy0ZiGOayHYm")
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