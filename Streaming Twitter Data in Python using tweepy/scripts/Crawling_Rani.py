#author : Yuwono Bangun Nagoro (a.k.a SurgicalSteel)
import tweepy
auth = tweepy.OAuthHandler("YOUR-CONSUMER-KEY","YOUR-CONSUMER-SECRET")
auth.set_access_token("YOUR-ACCESS-TOKEN","YOUR-TOKEN-SECRET")
api = tweepy.API(auth)
#rani=tweepy.api.get_user("raniapriana")
#print(rani.screen_name)
rani_tweet=api.user_timeline("raniapriana")
i=1
for twitnya in rani_tweet :
    print(str(i)+". "+"Rani Apriana says : "+twitnya.text)
    i+=1
