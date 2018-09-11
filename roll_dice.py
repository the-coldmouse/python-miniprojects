#This is just a beginer project to review my programming concepts.

import random

def roll_dice():
    """This returns a integer between 1-6 """
    return random.randint(1,6) 

while True:
    print("Rolling Dice:")
    import time
    time.sleep(3)
    print("You got a dice numbered: {}".format(roll_dice()))
    response = input("Do you wish to continue? (Y/N) ")  
    if (response == 'Y') or (response == 'y'):
        pass
    elif (response == 'N') or (response =='n'):
        print('Quitting!!!')
        exit()
    else:
        print('Invalid response')
        exit()


