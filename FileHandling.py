# -*- coding: utf-8 -*-

import io
import os

#Open a file in write and binary mode.
#path=os.path.abspath("c:/myfiles/demotxt.txt")
#fob = open(path, "r")
# fob = open('app.log', "r")
# print(fob)

# #Display file name.
# print("File name: ", fob.name)
# #Display state of the file.
# print("File state: ", fob.closed)
# #Print the opening mode.
# print("Opening mode: ", fob.mode)

# fob.close()



'''
f = open('app2.log', mode = 'r')
'''


# try:
#    f = open('app.log')
#    # do file operations.
# except FileNotFoundError as e:  
#         print("File Not Found")



'''
with open('app.log', 'w') as f:
   #first line
   f.write('my first file\n')
   #second line
   f.write('This file\n')
   #third line
   f.write('contains three lines\n')

with open('app.log', 'r') as f:
   content = f.readlines()

for line in content:
   print(line)
'''

'''
with open('app.log', 'w') as f:
   #first line
   f.write('my first file\n')
   #second line
   f.write('This file\n')
   #third line
   f.write('contains three lines\n')

f = open('app.log', 'r')
print(f.read(10))    # read the first 10 data
#'my first f'

print(f.read(4))    # read the next 4 data
#'ile\n'

print(f.read())     # read in the rest till end of file
#'This file\ncontains three lines\n'

print(f.read())  # further reading returns empty sting
#''
'''

with open('app.log', 'w') as f:
    #first line
    f.write('It is my first file\n')
    #second line
    f.write('This file\n')
    #third line
    f.write('contains three lines\n')
    f.close()

# #Open a file
try:
    f = open('app.log', 'r')
    data = f.read(19);
    print('Read String is : ', data)

#Reposition pointer at the beginning once again
    position = f.seek(0, 0);
    data = f.read(19);
    print('Again read String is : ', data)
except FileNotFoundError as e:
    print("File Not Found")
#Close the opened file
finally:
    f.close()


'''
import os
#Rename a file from <app.log> to <app1.log>
os.rename( "app.log", "app1.log" )
'''

'''
import os

#Delete a file <app1.log>
os.remove( "app.log" )
'''