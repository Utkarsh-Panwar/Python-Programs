# -*- coding: utf-8 -*-


# print("Hello, Python!")
# print('Second line')

# #Lines and Indentation
# if (True):
#     print("True \n hello")
# else:
#     print("False \n bye")



# if True:
#   print( "Answer")
#   print ("True")
# else:
#   print ("Answer")
#   print ("False" )



#variables-------------------
# counter=100          # An integer assignment
# miles   = 1000.0      # A floating point
# name    = "John"       # A string
# print(counter)
# print(miles)
# print(name)



# Multiple Asignments----------------------
# a = b = c = 1
# print(a,b,c)
# a,b,c = 1,2.6,"john"
# print(a,b,c)

#python strings

# str = 'Hello World!'

# print(str)        # Prints complete string
# print(str[0])       # Prints first character of the string
# print (str[2:5] )    # Prints characters starting from 3rd to 5th
# print (str[2:] )     # Prints string starting from 3rd character
# print( str * 2  )    # Prints string two times
# print( str + " TEST" )# Prints concatenated string
# print(8+9) # + is arithmetic operator (addition)
# print("8"+'9') #+ is string operatore(concatinate)





#Pythons Lists--------------------
# lists = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']

# print(lists)         # Prints complete list
# print(lists[0])       # Prints first element of the list
# print(lists[1:3])     # Prints elements starting from 2nd till 3rd 
# print(lists[2:])      # Prints elements starting from 3rd element
# print(tinylist * 2)  # Prints list two times
# print(lists + tinylist) # Prints concatenated lists



#Python Tuple--------------------

# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')

# print(tuple)           # Prints complete list
# print (tuple[0])        # Prints first element of the list
# print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
# print (tuple[2:])       # Prints elements starting from 3rd element
# print (tinytuple * 2)   # Prints list two times
# print (tuple + tinytuple) # Prints concatenated lists



#--------------------Python Dictionary
# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"

# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


# print( dict['one'])       # Prints value for 'one' key
# print (dict[2])           # Prints value for 2 key
# print (dict)          # Prints complete dictionary
# print (tinydict.keys())   # Prints all the keys
# print (tinydict.values()) # Prints all the values
# print(tinydict['name'])


#----------------type casting----------------------------------


# a="10";b="20"
# print("The sum of ",a, " and ",b," is ",(a+b))
# print("The sum of "+a+" and "+b+" is "+(a+b))
# print("The sum of "+a+" and "+b+" is ",(int(a)+int(b)))

# a,b=10,20
# print("The sum of ",a," and ",b," is ",(a+b))




#------------------------------Arithmetic Operators---------------------------------------

# a,b=10,20
# print("+",a+b)
# print("-",a-b)
# print("*",a*b)
# print("/",a/b)
# print(10%3)
# print("%",a%b)
# print("//",a//b)
# print("**",a**b)



#--------------------------------Relational Operators---------------------------------

a,b=10,20
# if a==b:
#     print("Hello")
# else:
#     print("Bye");
    
# if a!=b:
#     print("Hello")
# else:
#     print("Bye")
    
# if a<b:
#     print("Hello")
# else:
#     print("Bye")
    
# if a>b:
#     print("Hello")
# else:
#     print("Bye")
    
# if a<=b:
#     print("Hello")
# else:
#     print("Bye")
    
# if a>=b:
#     print("Hello")
# else:
#     print("Bye")



#----------------------------------------Logical Operators--------------------------------

# a,b=10,20
# if a<=10 and b>=30:
#     print("Hello")   
# else:
#     print("Bye")
    
# if a<=10 or b>=30:
#     print("Hello")   
# else:
#     print("Bye")

# if not(a<=10) or b>=30:
#     print("Hello")   
# else:
#     print("Bye")

#--------------Assignment
a,b=5,7
a+=b #a=a+b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b-1
print(a)
a%=b
print(a)
print(b)
a**=b
print(a)
a//=b
print(a)
