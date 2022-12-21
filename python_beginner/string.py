"""srtrings"""

# # srt() 

# # string - Unchangeble , ordered , indexeble internally data type
# string = "Hello"
# string2 = 'Hello'

# doc_srtring = """used for  writing documentation for few codelines"""

# doc_srtring2 = '''used for writing documentation '''

# # if i want to write in usual "" that's mistake 
# # string3 = 'Hello', I'm student #error

# doc_srtring4 = "Hello , I'm student "
# doc_srtring5 = "Hello , I\'m student " #ecronirovanie 

# str1 = 'Hello'
# srt2 = 'world'

# print(str1 + srt2 ) #Helloworld

# frog = 'Quak'
# print(frog * 3 ) #QuakQuakQuak

"""Function and method string"""

# greeting = 'Hello, world'
# # print(len(greeting))
# # len(x) = count all characters in code 

# print(dir(greeting))
# #dir(x) - returns list of method transmmited  objects

# #Method - function , definite data type and can be called through only one , method

# my_str = 'Hello world'

# print(my_str.lower())
# print(my_str.upper())

# print(my_str.split()) # srt.split() returns a list from strings by devisor if returns devisor - by space 

# my_str2 = '          hello world         '
# my_str2.title() # Hello World
# my_str2.capitalize() # Hello world
# my_str2.count('l') # 3
# my_str2.replace('o','n') # replace Hello wnrld
# print(my_str2.strip())
# my_str2.lstrip() # delete from left side
# my_str2.rstrip() # delete from right side

# str = "Some string with 5 words"
# str.isalpha() # false
# str.isdigit() # false
# str.islower() # true
# str.isupper() # true
# str.isalnum() # False 
# str.isspace() # true
# str.istitle() # true
# str.isnumeric() # true
# str.isdecimal() # true
# str.startswith('s') # true
# str.endswith('s') # False

# #in
# 'with' in str 

"""Foramatting / interpolation"""

# name = input('name') # cam be changeable
# party = input('party')
# # inv = 'Dear %s, we are happy to invaite you' % name 

# # inv2 = 'Dear {a1}, we are happy to invaite you on {b2}'.format(a1 = name,b2 = party)

# inv3 = f'Dear {name}, we are happy to invaite you on {party}'

# print(inv3)

"""Index and slices"""

# str10 = 'makers'
# str10[0] # 'm'
#indexes - ordinal number elements in string/list/cortge. Indextion start on 0
#"hello"
# 01234
# -5 -4 -2 -1 

# string2 = 'house'
# # print(string2[len(string2)-1])
# print(string2[-1])

# string3 = 'hello world'
# # start = 0
# # stop = 5
# # step = 1

# # print(string3[start: stop: step])

# # print(string3[::])

# print(string3[::-1])

"""ecronirovanie"""


# print('Hello\n\tworld')
# """
# Hello 
#     world
# """

# path = "c:\\users\\new\\tanks"
# print(path)

# "hello world" + "\n" *

a = lower(Hello)

print(a)