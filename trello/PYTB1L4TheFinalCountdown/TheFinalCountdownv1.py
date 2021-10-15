import time

count= 10

while True	:
 count= count - 1
 time.sleep(0.2)
 print (count)
 if count == 0:
     break