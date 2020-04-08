from random import randint
import time
a=randint(1,100)
b=int(input('enter number:'))
 
while True:
    if b<a:
        print ('entered number is lesser than random number')
    elif b>a:
        print ('entered number is bigger than random number')
    else:
        print('congratulations')
        break
    b=int(input('enter number:'))    
time.sleep(5)