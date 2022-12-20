"""If - elif - else """

# bool - Unchaingeble data type , which  has only 2 value: True or False

# 10 > 2 # True
# > - more 
# < - less
# <= - more or equal
# >= - less or equal
# == - equal
#!= - not equal
# < > less
# <= > more or equal
# >= > more or equal
#!= > not equal

#print(25 == 23) # False
# print(bool()) True = 1 ,  False = 0

#print(bool(2)) # True any number will be true if we will into bool
# print(bool(-2)) # True

# print(bool('it')) # True
# print(bool('')) # False

# bool() #False
# bool({}) #False
# bool(set()) #False
# bool(None) #False

"""if"""

# num = 10
# print("num")

# num = 15
# if num > 10:
#     print("num > 15")

"""if - else"""

# num = 15
# if num > 20:
#     print("num > 20")
# else:
#     print("num < 20")

# num = 15
# if num > 20:
#     print("num > 20")

# if num < 20:
#     print("num < 20")

# temperature = 40
# if temperature < 20:
#     print("Cold")
# else:
#     if temperature < 30:
#         print("Medium")
#     else:
#         if temperature > 35:
#             print("Hot")

"""if elif else"""

# temperature = 40
# if temperature < 20:
#     print("Cold")
# elif temperature < 30:
#     print("Medium")
# elif temperature > 35:
#     print("Hot")
# else:
#     print("Wrong temperature")

# num = 15
# if num < 20:
#     print("num < 20")
# elif num > 10:
#     print("num > 10")

# num = 15
# if num < 20:
#     print("num < 20")
# if num > 10:
#     print("num > 10")

# mark = input("Print mark from 1 to 5 ")
# msg = ''
# if mark.isdigit():
#     mark = int(mark)
#     if mark == 5:
#         msg = 'You have reached good mark'

#     elif mark == 4:
#           msg = 'You have reached normal mark'

#     elif mark <= 3:
#         msg = 'Your mark is suck'

#     print(msg)

# else:
#     print("You wrote note mark")

"""and , or , not"""

# age = 18
# if age >= 18 and age < 28:
#     print("You welcome")
# else:
#     print("You are not welcome")

False # False
True # True

False and False # False
True and True # True
False and True # False
True and False # False

False or False # False
True or True # True
False or True # True
True or False # True

not True # False
not False # False

(False or True) and (False or False) # False

"""is, ==, in """

# a = 10
# print(a is 10 )

# a = 10
# b = 10 
# print(id(a))
# print(id(b))

# string = 'hello world'
# print('world' in string)

"""ternary operator"""

# msg = input("write message")
# if len(msg) > 10:
#     print('Your message longer than 10 ')
# else:
#     print('Your message is less than 10 ')

msg = input("write message ")
res = 'Your message longer than 10' if len(msg) > 10 else"Your message is less than 10"
print(res)





