"""Lists , Loops: for , while"""

# list()
# list() - collections of elements. Changeable , ordered  , indexed data types. Use for keeping collections of elements
# Elements of the list can be any data types

list_with_all_data_types = [1, "string", True, False, None, [1,2],{'a', 10},{1,2},('a',1,'b')]
# print(list_with_all_data_types)

list_of_numbers = [1 , 2 , 3 , 4 , 5 , [6 , 7]]
list_of_numbers[0] #1
list_of_numbers[1] #2
list_of_numbers[2] #3
list_of_numbers[3] #4
list_of_numbers[4] #5
list_of_numbers[5] #[6 , 7]
list_of_numbers[5][1] #7

list_of_numbers[1:3:] # [2 , 3]

"""Method of list"""

"""1)How add elements to list"""

# a = [1 , 2 , 3]
# print('before', a)
# a.append(4) # add an element to end of list
# print('after', a)

# a = '123'
# a + '4'
# print(a) # 123

# a.insert(0 , 'element')
# print(a)

#a.insert(index , element) # add element on specified index

# a.insert(len(a), '4')
# print(a) 

list1  =[1 , 2 , 3]
list2 = [4 , 5 , 6]

# list1.extend(list2)  # [1, 2, 3, 4, 5, 6]
# print(list1)

# new_list = list1 + list2
# print(new_list)

"""Changing elements"""

# letters = ['a' , 'b' , 'c' , 'g']
# letters[3] = 'd'
# print(letters)

"""Deleting elements"""

# letters = ['a' , 'b' , 'c' , 'g']
# letters.pop(2)
# print(letters)


# letters = ['a' , 'b' , 'c' , 'g']
# deleted_el = letters.pop(2)
# print(deleted_el)

# letters = ['a' , 'a', 'b' , 'c' , 'g']
# # letters.remove('a')
# # print(letters)
# # letters.remove('adsffd') # Value Error

# # letters.clear() 
# # print(letters)

# del letters[1]
# print(letters) # ['a', 'b', 'c', 'g']

"""sorting and copying"""

# nums = [1 , 2 , 3 , 4]
# nums_copy = nums.copy()
# nums_copy2 = nums[:]
# print(nums_copy2)

# nums = [1 , 2 , 3 , 4]
# nums2 = nums
# nums2.append(5)
# print(nums2)
# print(nums)
# print(nums is nums2)

# nums_list = [8 , 6 , 10 , 5]
# # nums_list.sort()
# nums_list.sort(reverse=True)
# print(nums_list)

# names = ['Kanne', 'Johannes', 'Jerry', 'Tom']
# names.sort(key=len , reverse=True)
# # names.sort(key=len)
# print(names)

# names = ['Kanne', 'Johannes', 'Jerry', 'Tom']
# sort = sorted(names) 
# print(sort)

# names.reverse()

"""cycles"""
# Cycles - completing one of the part of code 

# Intertions - repeating any muvement

#

# nums_list = [1, 2, 3, 4, 5]
# print(nums_list[0])
# print(nums_list[1])
# print(nums_list[2])
# print(nums_list[3])
# print(nums_list[4])

# 1) for
# nums_list = [1, 2, 3, 4, 5]
# for num in nums_list:
#     print(num)

# for  - cycle , which is going through every element in integreted object and keep working until this elements will end 
# for - element in integreted_ob
        #body cycle

# string = "Hello, world"
# for letter in string:
#     print(letter)

# nums = range(10)
# for num in nums:
#     print(num)

nums = range(1, 21)
new_nums = []
for num in range(1,21):
    if num % 2 == 0:
        new_nums.append(num)
        
print(new_nums)