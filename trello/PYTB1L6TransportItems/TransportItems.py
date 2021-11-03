import os
import time

factory = ["factory: ","fiets"]
distribution = ["distribution: ",]
shop = ["shop: ",]

os.system('cls')
print (factory)
print (distribution)
print (shop)
factory.remove("fiets")
distribution.append("fiets")
time.sleep(2)
os.system('cls')

print (factory)
print (distribution)
print (shop)
distribution.remove("fiets")
shop.append("fiets")
time.sleep(2)
os.system('cls')

print (factory)
print (distribution)
print (shop)
shop.remove("fiets")
time.sleep(2)
os.system('cls')


