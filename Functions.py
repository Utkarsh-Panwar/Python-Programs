# -*- coding: utf-8 -*-
# def hello():
#     print("Hello World") 
#     return("hello")

# def hello_noreturn():
#     print("Hello World")
  
# a=hello()
# print(a)
# print(hello())
# a=hello_noreturn() 
# print(a)



#def run():
#     for x in range(10):
#         print(x)
#  
#run()




## Define `plus()`
#def plus(a,b):
#   sum = a + b
#   return (sum, a)
#
# # Call `plus()` and unpack variables 
#sum, a = plus(3,4)
#
# # Print `sum()`
#print("Sum of 3 and 4 is ",sum)
#print("The value of a is ",a)
#print("Printing plus ",plus(34,56))



# # Define `plus()` function
# def plus(a,b = 2):
#   return a + b
  
# # Call `plus()` with only `a` parameter
# a=plus(a=1)
# print( "With value of a ",a)
# # Call `plus()` with `a` and `b` parameters
# a=plus(a=1, b=3)
# print( "With value of a and b",a)



# # Define `plus()` function
# def plus(a,b):
#   return a + b
  
# # Call `plus()` function with parameters 
# a=plus(2,3)
# print("with value ",a)
# # Call `plus()` function with keyword arguments
# a=plus(b=1, a=2)
# print("With strict values ",a)



##Define `plus()` function to accept a variable number of arguments
#def plus(*args):
#   total = 0
#   for i in args:
#     total += i
#   return total
#
# # Calculate the sum  
#a=plus(20,30,40,50)
#print("Function with multiple arguments ",a)



# Global variable `init`
init = 1

# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  # Local variable `sum()`
  total = 0
  for i in args:
    total += i
  print(init)  
  return total
  
# Access the global variable
print("this is the initialized value " + str(init))
#print(plus(20,40,50,60)
#(Try to) access the local variable
#print("this is the sum " + str(total))



#Lamda Functions-----------------------


#double = lambda x: x*2
#
#a=double(5)
#print( a)



'''
# `sum()` lambda function
sum = lambda x, y: x + y

# Call the `sum()` anonymous function
a=sum(4,5)
print("Output of lamda is ",a)
# "Translate" to a UDF
def sum(x, y):
  return x+y

a=sum(3,8)
print("Output of def ",a)
'''


my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list =list(filter(lambda x:(x*2 > 10), my_list))

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))


print(filtered_list)
print(mapped_list)



# ## Define `main()` function
# def main():
#   print("This is a main function")

# main()
