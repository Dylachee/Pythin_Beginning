"""comprehensions(generators)"""

# list_ = []
# for i in range(1,6):
#     list_.append(i)
# print(list_)

# list_ = [i for i in range(1,6)]
# print(list_)

# comprehension - short way to write cycle for creating collections

# cyntaxis_generator = [expression for expression in integrable object]

# 1) add to list 10 numbers from 1 to 10

# nums = []
# for num in range(1 , 10):
#     nums.append(num)
# print(nums)

# nums = [num for num in range(1,10)]
# print(nums)

# 2) write in list of numbers , and add for every number +10

# num_10 = []
# # for num in range(1,6):
# #     num_10.append(num + 10)
# # print(num_10)

# num_10 = [num + 10 for num in range(1,6)]
# print(num_10)

# 3) Write to list numbers from 1 to 10, and only use numbers 2.4.6.8

# even_nums = []
# for num in range(1,10):
#     if num % 2 == 0:
#         even_nums.append(num)
# print(even_nums)

# even_nums = [num for num in range(1,10) if num % 2 == 0]
# print(even_nums)

# cintaxis_generator_with_condition = [expression for expression in integrable if expression]

# 4) write in the list numbers from 1 to 10 , chtnym add +10 , nechtnym +200

# nums_200 = []
# for num in range(1,10):
#     if num % 2 == 0:
#         nums_200.append(nums_200 +10)
#     else:
#         nums_200.append(nums_200 + 200)
# print(nums_200)

# nums_200 = []
# for num in range(1,10):
#     nums_200.append(num + 10) if num % 2 == 0 else nums_200.append(num + 200)
# print(nums_200)

# generated_nums_200 = [num + 10 if num % 2 == 0 else num + 200 for num in range(1,10)]

# cyntaxis_generator_with_two_expressions = [ternal_operator for expression in integreble_object]

# 5) write to the list numbers in random range , and for chetnum +10 , for nechetnum add 200 , but work only with

# import random

# random_num = random.randrange(5,20)
# nums_with_3_exp = []
# for num in range(1, random_num):
#     if num > 5:
#         if num % 2 == 0:
#             nums_with_3_exp.append(num + 10)
#         else:
#             nums_with_3_exp.append(num + 200)
# print(nums_with_3_exp)


# nums_with_3_exp1 = [num + 10 if num % 2 == 0 else num + 200 for num in range(1, random_num) if num > 5]
# print(nums_with_3_exp1)

"""dict comprehension"""

# ranhe(1,10) - itetarator 

# generator = [*(num for num in range(1,6))]
# print(generator)

r = range(1,8)
for i in r:
    print(r)
for i in r:
    print(r)   
for i in r:
    print(r)