import random
import time
import sys


#generates random number
def num_generator(value=6):
    gen_key = random.randint(0,value)
    return gen_key


#contains destination list and will randomly generate destination for user
def get_destination(des_key):
    potential_des = {1: 'tokyo',2: "norway",3: 'greece',4: 'toronto',5: 'hawaii',6: 'seoul'}
    value = potential_des.get(des_key)
    return value
    
def get_restaurant(des_name = 'tokyo'):
    restaurant_choices = {'tokyo': ['a'], 'norway': ['b'],'greece': ['c'], 'toronto': ['d'], 'hawaii': ['e'], 'seoul': ['f']}
    value = restaurant_choices.get(des_name)

    return value 
   



#num = 0 
"""while num != 8:
    num = num_generator(8)
    print(num)"""
#test = get_restaurant()
#print(test)


