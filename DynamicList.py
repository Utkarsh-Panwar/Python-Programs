# -*- coding: utf-8 -*-

list=[];k=0;l=0;max=0
a=int(input('Enter limit for columns '))
for x in range(a):
    b=int(input('Enter element for '+str(x)+' index '))
    list.append(b)
    if(list[x]>max):
        max=list[x]
    if(list[x]%2==0):
        k=k+list[x]
    else:
        l=l+list[x]
        
print("Sum of even is ",k)
print("Sum of odd is ",l)
print(max," Is the greatest number")    
