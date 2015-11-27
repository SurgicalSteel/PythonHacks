#Created by Yuwono Bangun Nagoro a.k.a SurgicalSteel
#Using Pycharm Community Edition 5.0.1 for Python 3
#Date Created : November 27, 2015
import pyowm
def get_weather_data(city) :
    owm=pyowm.OWM("b65801209e754b349eb2d3233a39869c")
    current=owm.weather_at_place(city)
    ldata=current.get_location()
    wdata=current.get_weather()
    print(ldata.get_name()+", "+ldata.get_country())
    print("Latitude\t\t: "+str(ldata.get_lat()))
    print("Longitude\t\t: "+str(ldata.get_lon()))
    print("Weather\t\t\t: "+wdata.get_status()+", "+wdata.get_detailed_status())
    tdata=wdata.get_temperature('celsius')
    print("Temperature\t\t: "+str(tdata['temp'])+" Celsius")
    pdata=wdata.get_pressure()
    print("Pressure\t\t: "+str(pdata['press']))

city=input()
get_weather_data(city)




