#-------------------------------------------------------------------------------
# Name:        test Request by Country and City
# Purpose:     Test consume JSON aja gituh dari locu
#
# Author:      Yuwono Bangun Nagoro
#
# Created:     25/11/2015
# Copyright:   (c) Yuwono Bangun Nagoro 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib.request

import json
def locu_search(country,city) :
    locu_api="ba5a693ee9ebd16c2b891273b34d0674d00c89f1"
    urlreq="https://api.locu.com/v1_0/venue/search/?country="+str(country)+"&locality="+str(city)+"&api_key="+str(locu_api)
    json_obj=urllib.request.urlopen(str(urlreq))
    data=json.loads(json_obj.readall().decode('utf-8')) #.load(json_obj)
    i=1
    for item in data['objects'] :
        print(str(i)+".name : "+item['name'])
        if item['lat']!= None :
            print ("     latitude : "+str(item['lat']))
        if item['long']!= None :
            print ("     longitude : "+str(item['long']))
        if item['street_address']!=None :
            print ("     address : "+str(item['street_address']))
        print(' ')
        i+=1
country=input()
city=input()
locu_search(country,city)



