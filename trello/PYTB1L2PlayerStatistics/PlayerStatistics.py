from typing import get_origin


while True:

    name= ("Mauro Hendriks")
    lives= 2.5
    wizard= False
    thief= True
    mage= False
    level= 20
    special= ("jump slash")
    weapon= ("daggers")
    speed= 210
    defence= 120
    pet= ("cat")
    petn= ("void")
    petl= ("8")

    print (name)
    print ("lives left:" + str(lives))

    if wizard == True: 
      print ("class:wizard level:" + str(level))  
       
        
    if thief == True: 
        print("class:thief level:" + str(level))
       
        
    if mage == True:
        print ("class:mage level:" + str(level)) 
    

    print ("special:" + special)
    print ("weapon:" + weapon)
    print ("speed:" + str(speed))
    print ("defence:" + str(defence))
    print ("pet:" + petn + " the " + pet)  
    print ("pet's lives left:" + str(petl)) 
    break         