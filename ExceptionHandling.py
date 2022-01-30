
# -*- coding: utf-8 -*-
import sys

# a=10/0
# print(a)


# a=int(input("Enter first number "))
# b=int(input("Enter second number "))
# result=a/b
# print(result)


#try:  
#    a=int(input("Enter first number "))
#    b=int(input("Enter second number "))
#    result=a/b
#    print(result)
#except ValueError as e:  
#        value,type,stacktrace=sys.exc_info()
#        print("value : ",value,"\n","type : ",type,"\n","stacktrace : ",stacktrace)
#        print("Plz only enter numbers")    
#        print(e)
#except ZeroDivisionError as e:  
#        value,type,stacktrace=sys.exc_info()
#        print("value : ",value,"\n","type : ",type,"\n","stacktrace : ",stacktrace)
#        print("Cannot divided by zero")  
#              
#finally:  
#    print("Welcome" )



def initarr(a):
    if(a<=0):
        raise Exception("Only enter positive value")
    else:
        for i in range(0,a):
            print(i+1)

num=int(input("Enter a number "))
try:
    initarr(num)
except Exception as e:
    print(e)
