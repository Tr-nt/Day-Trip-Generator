import random
import time
import sys


#generates random number
def num_generator(value=6):
    gen_key = random.randint(0,value)
    return gen_key


#contains destination list and will randomly generate destination for user
def get_destination(des_key):
      potential_des = {1: 'Tokyo, Japan',2: "Oslo, Norway",3: 'Athens, Greece',4: 'Toronto, Canada',5: 'Honolulu, Hawaii',6: 'Seoul, South Korea'}
    value = potential_des.get(des_key)
    return value
    
# contains restaurant dict and will randomly generate restaurant for user
def get_restaurant(des_name = 'tokyo'):
    restaurant_choices = {'Tokyo, Japan': ['Toufuya Ukai','Narisawa','Gyukatsu Motomura Harajuku'], 'Oslo, Norway': ['Restaurant Fjord','Hos Thea','Lofoten Fiskerestaurant'],'Athens, Greece': ['Maiandros Resturant', 'Lithos Tavern', 'Tudor Hall'], 'Toronto, Canada': ['Auberge du Pommier', 'Canoe', 'Richmond Station'], 'Honolulu, Hawaii': ['Senia', 'Moku Kitchen','Ono Seafood'], 'Seoul, South Korea': ['Jungsik Seoul', 'Maple Tree House', 'Ryunique']}
    value = restaurant_choices.get(des_name)

    return value 
   



#num_value = num_generator()

#key_value = get_destination(num_value)

#res_value = get_restaurant(key_value)

#print(num_value,key_value,res_value)

#num = 0 
"""while num != 8:
    num = num_generator(8)
    print(num)"""
#test = get_restaurant()
#print(test)


