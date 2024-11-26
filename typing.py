from time import *
import random as r
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error+=1
        except:
            error+=1
    return error
def speed(times,timee,userinput):
    timedelay=timee-times
    timer=round(timedelay,2)
    speed=len(userinput)/timer
    return round(speed)
while 1:
    ck=input(" Are you Ready to test.Give yes/no: ")
    if ck=="yes":
        test=["Technology is the exploration of scientific knowledge to develop tools and techniques to transform the world by improving efficiency in almost everything we do.","Technology is the study of scientific knowledge in order to create tools and processes.","The definition of technology is the application of scientific knowledge for practical purposes or applications."]
        test1=r.choice(test)
        print("*****typing test******")
        print(test1)
        print()
        print()
        time1=time()
        testinput=input("enter:")
        time2=time()
        print("Speed:",speed(time1,time2,testinput),"w/sec")
        print("Error:",mistake(test1,testinput))
    elif ck=="no":
        print("THANKYOU")
        break
    else:
        print("WRONG INPUT")
