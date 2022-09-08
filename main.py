import random
import time
import sys
from webbrowser import get

def day_generator():

    #Prints welcome message 
    def welcome_message():
        print("Welcome to Day Trip Generator!")


    #Prints validation message
    def validator_message():
        print("\nDid you like the selection?\nPlease type Y for Yes or N for No to continue.")
    

    #validates state with bool value
    def validator():
        valid = 'y' 
        invalid = 'n'
        
        validator_message()
        
        check = str(input()).lower()

        if check == valid:
            return True
        elif check == invalid:
            return False
        elif check != valid and check != invalid:
            print("That was an invalid input\n")
            return validator()
            

    #Randomly generates destination value
    def get_destination():
        destination_dict = {0: 'Tokyo, Japan',1: "Oslo, Norway",2: 'Athens, Greece',3: 'Toronto, Canada',4: 'Honolulu, Hawaii',5: 'Seoul, South Korea'}
        
        value = random.choice(destination_dict)
        
        time.sleep(1)
        print(f"Your destination is {value}!")
        
        is_valid = validator()
        
        if is_valid == False:
            return get_destination()
        return value 
    
    
    # Randomly generates transportation value
    def get_transportation():
        transport = random.choice ([ 'Rental Car', 'Bus', 'Bicycle', 'Train', 'Walking'])
        
        time.sleep(1)
        print(f"Your mode of transport is {transport}!")
        
        is_valid = validator()
        if is_valid == False:
            return get_transportation()
        return transport
    

    # Randomly generates restaurant value
    def get_restaurant(name_key):
        restaurant_choices = {'Tokyo, Japan': ['Toufuya Ukai','Narisawa','Gyukatsu Motomura Harajuku'], 'Oslo, Norway': ['Restaurant Fjord','Hos Thea','Lofoten Fiskerestaurant'],'Athens, Greece': ['Maiandros Resturant', 'Lithos Tavern', 'Tudor Hall'], 'Toronto, Canada': ['Auberge du Pommier', 'Canoe', 'Richmond Station'], 'Honolulu, Hawaii': ['Senia', 'Moku Kitchen','Ono Seafood'], 'Seoul, South Korea': ['Jungsik Seoul', 'Maple Tree House', 'Ryunique']}
        
        value = random.choice(restaurant_choices.get(name_key))
        
        print(f"The restaurant you are going to is {value}")
        
        time.sleep(1)
        
        is_valid = validator()
        
        if is_valid == False:
            return get_restaurant(name_key)
        return value


    #Randomly generates activities value
    def get_activity(name_key):
        active_list = {'Tokyo, Japan': ['Tokyo Disneyland', 'Shinjuku Gyoen National Garden', 'Ninja Museum'], 'Oslo, Norway': ['Viking Ship Museum','Vigeland Park','Oslo Opera House'],'Athens, Greece': ['Acropolis','Psiri','The National Gardens'], 'Toronto, Canada': ['CN Tower','Toronto Zoo','Graffiti Alley'], 'Honolulu, Hawaii': ['Wakiki Beach','Manoa Falls','Bishop Museum'], 'Seoul, South Korea': ['Gyeongbokgung Palace','National Museum at Korea','Namsan']}
        
        name_values = random.choice(active_list.get(name_key))
        
        time.sleep(1)
        
        print (f"You will be going to {name_values} as your activity!")

        is_valid = validator()
        
        if is_valid == False:
            
            return get_activity(name_key)
        
        return name_values

    def sys_validate():
        valid = 'y' 
        invalid = 'n'
        
        time.sleep(1)
        print("Do you like your vacation choices? ")
        
        check = str(input()).lower()

        if check == valid:
            sys.exit()
        elif check == invalid:
           return day_generator()
        elif check != valid and check != invalid:
            print("That was an invalid input\n")
            return sys_validate()


    
    welcome_message()
    active = True
    while active:                      
        destination = get_destination()
        get_transportation()
        get_restaurant(destination)
        get_activity(destination)
        sys_validate()
        
day_generator()


