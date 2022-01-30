# -*- coding: utf-8 -*-
'----------------------------------------If Else------------------------------------------------'

# a=1
# if a==1:
#     print("One")
#     print("First Block is true")
# elif a==2:
#     print("Two")
#     print("Second Block is true")
# else:
#     print("Sorry")
#     print("Else block is true")


# a=2;b=3
# if(a==1):
#     if(b==2):
#         print("b is 2")
#     else:
#         print("b is not 2")
#     print("a is 1")
# else:
#     print("a is not 1")
    

# day=input("Enter a number between 1-7\n")
# #day=int(input("Enter a number between 1-7"))
# #if(day==1):
# if(day=="1"):
#     print("Sunday")
# elif(day=="2"):
#     print("Monday")
# elif(day=="3"):
#     print("Tuesday")
# elif(day=="4"):
#     print("Wednesday")
# elif(day=="5"):
#     print("Thursday")
# elif(day=="6"):
#     print("Friday")
# elif(day=="7"):
#     print("Saturday")
# else:
#     print("Sorry u entered a wrong number")



# a=input("Enter first number ")
# b=input("Enter second number ")
# print("The sum of ",a," and ",b," is ",(a+b))
# print("The sum of "+a+" and "+b+" is ",(a+b))

# print("The sum of ",a," and ",b," is ",(int(a)+int(b)))


'''
a=int(input("Enter first number "))
b=int(input("Enter second number "))
print("The sum of ",a," and ",b," is ",(a+b))
#print("The sum of "+a+" and "+b+" is ",(a+b))wrong
'''



# a=int(input("Enter first number "))
# b=int(input("Enter second number "))
# c=int(input("Enter third number "))   

# if a>b and a>c:
#     print(a," is the greatest number")
# elif b>a and b>c:
#     print(b," is the greatest number")
# else:
#     print(c," is the greatest number")




'----------------------------------------------------------------For Loop----------------------------'
#print("First Loop-------------------------------------")
'''
for x in range(5):   #for(x=0;x<5;x++)
    print(x)
'''

'''
for x in range(10,0,-1):#for(x=10;x>0;x--)
    print(x)
'''
#print("Second Loop-------------------------------------")

# Prints out 3,4,5
'''
for x in range(3, 6):
    print(x)
'''
#print("Third Loop-------------------------------------")



# #Prints out 3,5,7
# for x in range(3, 8, 2):
#     print(x)



# a=int(input("Enter a number"))
# for x in range(1,11):
#     print(a,"*",x,"=",a*x)
   
   
# print ("Pattern A")
# n = 0
# for x in range (0,11):
#     n = n + 1
#     for a in range (0, n):
#         print ('*',end='')
#     print()


# print ("Pattern B")
# for b in range (0,11):
#     n = n - 1
#     for d in range (0, n):
#         print ('*',end='')
#     print()

# print ("Pattern C")
# for e in range (11,0,-1):
#     print((11-e) * ' ' + e * '*')

# print ('')
# print ("Pattern D")
# for g in range (11,0,-1):
#     print(g * ' ' + (11-g) * '*')




# n=5
# x=1
# for e in range(1,6):
#     n=n-1
#     print(n*' '+x * '*')
#     x+=2

  
'----------------------------------------------------While -------------------------------Loop-------------'


# counter = 1

# while counter < 3:
#     print("Inside loop")
#     counter=counter+1




num = int(input("Enter a number: "))  
arm=0;sum=0;rev=0
temp = num  
  
while temp > 0:  
  digit = temp % 10  
  arm += digit ** 3  
  sum+=digit
  rev=(rev*10)+digit
  temp = temp//10
  
if num == arm:  
  print(num,"is an Armstrong number")  
else:  
  print(num,"is not an Armstrong number")  

print("Sum of ",num," is ",sum)
print(num," In reverse order is ",rev)

if(rev==num):
    print(num," is a palindrome number")
else:
    print(num," is not a palindrome number")
    
