#author : Yuwono Bangun Nagoro (a.k.a SurgicalSteel)

from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import tweepy
auth = tweepy.OAuthHandler("8FFhYU4Uf2uNxqB2PWDCkOF3y","za03dIX7yR1L9ZBzTVDbnBzK4A3tA7EJzmyY909vgAeVbg8cGB")
auth.set_access_token("206679796-MWUsxrgOU0K6USKX5AvC12J0GlwZ9lRVxO3VD67m","IPg2fOqq0u558isQn9WYYuOGxORimf76hWy0ZiGOayHYm")
api = tweepy.API(auth)

class mylistener(StreamListener):
    def on_data(self,data):
        mydata=json.loads(data) #as known before that 'data' is a string type variable, so I can just perform json.loads
        print (mydata['user']['name']+" (@"+mydata['user']['screen_name']+") : "+mydata['text'])
        #print(data)
        return True
    def on_error(self,status):
        print(status)

if __name__=='__main__':
    listen=mylistener()
    stream=Stream(auth,listen)
    stream.filter(track=['Yogyakarta']) #use 'Yogyakarta' as keyword