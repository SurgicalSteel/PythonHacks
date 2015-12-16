#author : Yuwono Bangun Nagoro (a.k.a SurgicalSteel)
import tweepy
auth = tweepy.OAuthHandler("8FFhYU4Uf2uNxqB2PWDCkOF3y","za03dIX7yR1L9ZBzTVDbnBzK4A3tA7EJzmyY909vgAeVbg8cGB")
auth.set_access_token("206679796-MWUsxrgOU0K6USKX5AvC12J0GlwZ9lRVxO3VD67m","IPg2fOqq0u558isQn9WYYuOGxORimf76hWy0ZiGOayHYm")
api = tweepy.API(auth)
#rani=tweepy.api.get_user("raniapriana")
#print(rani.screen_name)
rani_tweet=api.user_timeline("raniapriana")
i=1
for twitnya in rani_tweet :
    print(str(i)+". "+"Rani Apriana says : "+twitnya.text)
    i+=1