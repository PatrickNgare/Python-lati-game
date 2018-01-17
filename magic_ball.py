import random
answer=input("do you like football Yes/no:")
answer=random.randint(1,8)
print(answer)
if answer==1:
    print ("It is decidedly so")
elif answer==2:
    print ("Dont count on it")
elif answer==3:
    print ('Reply hazy try again')
elif answer==4:
    print ('Concentrate and ask again')
elif answer==5:
    print ('Cannot predict now')
elif answer==6:
    print ('Better not tell you now')
elif answer==7:
    print ('My reply is no')

elif answer==8:
    print ('Ask again later')
