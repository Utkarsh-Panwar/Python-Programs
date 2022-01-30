# -*- coding: utf-8 -*-
# a="my name is Utkarsh Panwar"
# print(a[0])
# print(len(a))
# print(a.capitalize())
# print(a)
# a="UTKARSH"
# print(a.casefold())
# print(a.count("e"))
# a="my name is utkarsh panwar"
# if(a.startswith("my")):
#     print("Hello")
# else:
#     print("Bye")
    
# if(a.endswith("my")):
#     print("Hello")
# else:
#     print("Bye")
    
# str = 'xyz\t 12345\t abc'
    
# print(str.expandtabs(tabsize=5))
# print(a.find("utkarsh"))

# str = "This article is written in {}"
# print (str.format("Python")) 
  
# print ("Hello, I am {} years old !".format(18))  

# a = {'x':'John', 'y':'Wick'} 
# print("{x}'s last name is {y}".format_map(a)) 

# a="SundayMonday"
# print(a.index("n"))
# print(a.index("n",5))
# print(a.isalnum())
# print(a.isalpha())
# print(a.isdecimal())
# print(a.isdigit())
# print(a.isidentifier())
# print(a.islower())
# print(a.isprintable())
# print(a.isspace())
# print(a.isupper())

# list1 = ['1','2','3','4']  
# s = " "
# s = s.join(list1) 
# print(s) 

# print(a.replace("n","w"))

# a="My name is Utkarsh Panwar"
# print(a.split(" "))

# a="                    Hello"
# print(a)
# print(a.strip())

a=input("Enter a string ")
reverse=""
for x in range(len(a)-1,-1,-1):
    reverse=reverse+a[x]
    
if(reverse==a):
    print(a," is a palindrome string")
else:
    print(a," is not a palindrome string ")