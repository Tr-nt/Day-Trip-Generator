import random
import time
import sys

def day_generator():
    #generates random number
    def num_generator(value=5):
        gen_key = random.randint(0,value)
        return gen_key


    #Randomly generates destination
    def get_destination(des_key):
        potential_des = {0: 'Tokyo, Japan',1: "Oslo, Norway",2: 'Athens, Greece',3: 'Toronto, Canada',4: 'Honolulu, Hawaii',5: 'Seoul, South Korea'}
        value = potential_des.get(des_key)
        return value
    
    # Randomly generates restaurant
    def get_restaurant(des_name):
        restaurant_choices = {'Tokyo, Japan': ['Toufuya Ukai','Narisawa','Gyukatsu Motomura Harajuku'], 'Oslo, Norway': ['Restaurant Fjord','Hos Thea','Lofoten Fiskerestaurant'],'Athens, Greece': ['Maiandros Resturant', 'Lithos Tavern', 'Tudor Hall'], 'Toronto, Canada': ['Auberge du Pommier', 'Canoe', 'Richmond Station'], 'Honolulu, Hawaii': ['Senia', 'Moku Kitchen','Ono Seafood'], 'Seoul, South Korea': ['Jungsik Seoul', 'Maple Tree House', 'Ryunique']}
        values = restaurant_choices.get(des_name)
        index = num_generator(2)
        list_value = values[index]
        return list_value 

    # Randomly generates transportation
    def transportation(des_key):
        transport_choices = {0: 'Rental car', 1: 'Bus', 2: 'Bicycle', 3: 'Train', 4: 'Walking'}
        transport = transport_choices.get(des_key)
        return transport
    
    #Randomly generates activities
    def activities(des_name):
        active_list = {'Tokyo, Japan': ['Tokyo Disneyland', 'Shinjuku Gyoen National Garden', 'Ninja Museum'], 'Oslo, Norway': ['Viking Ship Museum','Vigeland Park','Oslo Opera House'],'Athens, Greece': ['Acropolis','Psiri','The National Gardens'], 'Toronto, Canada': ['CN Tower','Toronto Zoo','Graffiti Alley'], 'Honolulu, Hawaii': ['Wakiki Beach','Manoa Falls','Bishop Museum'], 'Seoul, South Korea': ['Gyeongbokgung Palace','National Museum at Korea','Namsan']}
        
        values = active_list.get(des_name)
        index = num_generator(2)
        list_value = values[index]
        return list_value 



