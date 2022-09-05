import random
import time
import sys


#generates random number
def num_generator():
    random_num = random.randint(0,6)
    return random_num


#contains destination list and will randomly generate destination for user
def get_destination(des_key):
    potential_des = ['Tokyo','Norway','Greece','Toronto','Hawaii','Seoul']

def get_restaurant(des_key):
    destination_keys = {1 : 'tokyo', 2 : 'norway', 3 : 'greece',4 : 'toronto', 5: 'hawaii', 6: 'seoul'}
    value = destination_keys.get(des_key)
    return value 
   



