
import datetime

x = datetime.datetime.now()

print("Hello you!, ik ben Mauro Hendriks")
n = input("wie ben jij?")
print("Hello,", n+"!")
print(x.strftime("%c"))

answer = input("Enter y or n: ") 
if answer == "y": 
    pass
elif answer == "n": 
    print("dankjewel")

else: 
    print("again y/n.") 