# **1-Write a Python program to calculate the length of a string using 2 ways
string = input()
print(len(string))
count = 0
for i in string:
    count += 1
print(count)

# **2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead
# string1 = input()
#
# if (len(string1) < 2):
#     print(" ")
# else:
#     print(string1[:2]+string1[-2:])

# **3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# string = input()
# if len(string) >= 3:
#     if string[-3:] == "ing":
#         string += "ly"
#     else:
#         string += "ing"
# print(string)

# **4-Write a Python function that takes a list of words and return the longest word and the length of the longest one
# def longestWord(list):
#     longestnumber = 0
#     longestword = ""
#     for i in list:
#         if longestnumber < len(i):
#             longestnumber = len(i)
#             longestword   = i
#     print(longestnumber, longestword)
#
# list = ["taha", "mohamed", "ahmed", "mostafa"]
# longestWord(list)

# 5-Write a Python program to change a given string to a newly string where the first and last chars have been exchanged
# string = input()
# string = string[-1] + string[1:-1] + string[0]
# print(string)

# **6-Write a Python program to remove characters that have odd index values in a given string
# string = input()
# string1 = ""
# for i in range(0, len(string), 2):
#     string1 += string[i]
# print(string1)

# **7-Write a Python program to count the occurrences of each word in a given sentence
# sentence = input()
# words = sentence.split()
#
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# print("Word count:")
# for word, count in word_count.items():
#     print(word, count)

# 8-Write a Python script that takes input from the user and displays that input back in upper and lower cases
# string = input()
# print(string.upper())
# print(string.lower())

# 9-Write a Python function to reverse a string if its length is a multiple of 4
# string = input()
# if (len(string) % 4 == 0):
#     print(string[::-1])

# **10- Write a Python program to remove a newline in Python
# string = input()
# string = string.replace("\n", "")
# print(string)

# **11-Write a Python program to check whether a string starts with specified characters
# string = input()
# specifiedCharacters = "hello"
# if string.startswith(specifiedCharacters):
#     print("Yes")
# else:
#     print("No")

# **12- Write a Python program to add prefix text to all of the lines in a string
# string = "alahly is an egyptian football team \nahly gedda is an saudi arabian football team"
# prefix = "Hello: "
# prefixedString = prefix + string.replace("\n", "\n"+prefix)
# print(prefixedString)

# *13-Write a Python program to print the following numbers up to 2 decimal places
# list = [1.234, 3.34434, 2.34, 5, 5.8343]
# for i in list:
#     print("%.2f" % i)

# **14-Write a Python program to print the following numbers up to 2 decimal places with a sign
# list = [-1.234, 3.34434, -2.34, 5, 5.8343]
# for i in list:
#     print("{:+.2f}".format(i))

# **15-Write a Python program to display a number with a comma separator
# number = 123356215.22
# print("{:,.2f}".format(number))

# **16-Write a Python program to reverse a string
# first method
# string = input()
# print(string[::-1])
# #second method
# reversedString = ""
# for char in reversed(string):
#     reversedString += char
# print(reversedString)

# **17-Write a Python program to count repeated characters in a string
# string = input()
# dict = {}
# for char in string:
#     if char in dict:
#         dict[char] += 1
#     else:
#         dict[char] = 1
# for char in dict:
#     print(char, dict[char])

# **18-Write a Python program to find the first non-repeating character in a given string
# string = input()
# dict = {}
# for char in string:
#     if char in dict:
#         dict[char] += 1
#     else:
#         dict[char] = 1
# for char in dict:
#     if (dict[char] == 1):
#         print(char, dict[char])
#         exit(0)

# **19-Write a Python program to remove spaces from a given string
# string = input()
# string = string.replace(" ", "")
# print(string)

# **20-Write a Python program to count the number of non-empty substrings of a given string
# string = input()
# count = 0
# for i in range(len(string)):
#     for j in range(i+1, len(string)+1):
#         substring = string[i:j]
#         if len(substring) > 0:
#             count += 1
#
# print(count)

# **21-write a Python program to swap first and last element of any list.
# list = [1, 2, 3, 4]
# temp = list[0]
# list[0] = list[-1]
# list[-1] = temp
# print(list)

# **22-Given a list in Python and provided the positions of the elements.
# write a program to swap the two elements in the list.
# list = [1, 2, 3, 4]
# pos1 = int(input("please enter the first position: "))
# pos2 = int(input("please enter the second position: "))
# temp = list[pos1]
# list[pos1] = list[pos2]
# list[pos2] = temp
# print(list)

# **23- search for the all ways to know the length of the list
# list = [1, 2, 3, 4]
# #first way: using len()
# print(len(list))
# #second way: using any loop
# count = 0
# for i in list:
#     count += 1
# print(count)

# **24-write a Python code to find the Maximum number of list of numbers.
# list = [1, 100, 40, 34, 1000, 10]
# def findMax(list):
#     maxx = list[0]
#     for element in list:
#         if (element > maxx):
#             maxx = element
#     print(maxx)
# findMax(list)

# **25-write a Python code to find the Minimum number of list of numbers.
# list = [1, 100, 40, 34, 1000, 10]
# def findMax(list):
#     minn = list[0]
#     for element in list:
#         if (element < minn):
#             minn = element
#     print(minn)
# findMax(list)

# **26-search for if an elem is existing in list
# list = [1, 2, "taha", "hamada", 1.23]
# element = input()
# def findElement(list, element):
#     for i in list:
#         if i == element:
#             print("Found")
#             exit(0)
#     print("Not Found")
# findElement(list, element)

# **27- clear python list using different ways
# list = [1, 2, 3, 4]
# #first way: using clear() function
# list.clear()
# print(list)
# #second way:
# list = []
# print(list)
# #third way:
# list[:] = []
# print(list)
# #fourth way:
# del list[:]
# print(list)

# #**28-remove duplicated elements from a list
# list = [1, 2, 3, 1, 2, 3]
# newList = []
# for i in list:
#     if i not in newList:
#         newList.append(i)
# print(newList)

# **29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
# test_list = ["Taha", 3, "Ahmed", 8]
# key_list = ["name", "id"]
# j = 0
# result_list = []
# for i in range(len(test_list)):
#     result_list.append({key_list[j]: test_list[i]})
#     j += 1
#     if j == 2:
#         j = 0
#
# print(result_list)

# **30-write a python program to count unique values inside a list
# list = [1, 1, 2, 3, 3 ,3, 4, 4, 1, 2]
# print(len(set(list)))

# **31-write a python program Extract all elements with Frequency greater than K
# list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k = int(input())
# dic = {}
# for i in list:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# newList = []
# for i in dic:
#     if dic[i] > k:
#         newList.append(i)
# print(newList)

# **32-write a python program to find the Strongest Neighbour
# def find_strongest_neighbour(nums):
#     n = len(nums)
#     if n < 3:
#         return None
#     strongest = nums[1]
#     for i in range(2, n-1):
#         if nums[i] > strongest:
#             strongest = nums[i]
#     return strongest
#
# list = [1, 2, 3, 4, 5]
# strongest = find_strongest_neighbour(list)
# print(strongest)

# *33-write a Python Program to print all Possible Combinations from the three Digits
# def print_combinations(digits):
#     n = len(digits)
#     combination = [0] * n
#     used = [False] * n
#     def backtrack(pos):
#         if pos == n:
#             print(*combination, sep=' ')
#         else:
#             for i in range(n):
#                 if not used[i]:
#                     combination[pos] = digits[i]
#                     used[i] = True
#                     backtrack(pos+1)
#                     used[i] = False
#     backtrack(0)
#
# digits = [1, 2, 3]
# print_combinations(digits)

# **34-write a Python program to find all the Combinations in the list with the given condition
# list = [1, 2, 3]
# for i in range(len(list)):
#     for j in range(i+1, len(list)+1):
#         print(list[i:j])

# **35-write a Python program to get all unique combinations of two Lists
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         print(list1[i], list2[j])

# **36-Remove all the occurrences of an element from a list in Python
# list = [1, 1, 1, 2, 3, 3, 4, 5]
# removedItem = int(input())
# dic = {}
# for i in list:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# count = dic[removedItem]
# j = 0
# while j < count:
#     list.remove(removedItem)
#     j += 1
# print(list)

# #37-write a python program to Replace index elements with elements in Other List
# list1 = ["Gfg", "is", "best"]
# list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
# resultList = []
# for i in list2:
#     resultList.append(list1[i])
# print(resultList)

# **38- write python program to Retain records with N occurrences of K
# def retain_records(test_list, K, N):
#     return [record for record in test_list if record.count(K) == N]
#
# test_list = [(4, 5, 5, 4), (5, 4, 3)]
# K = 5
# N = 2
# result = retain_records(test_list, K, N)
# print(result)
#
# N = 3
# result = retain_records(test_list, K, N)
# print(result)

# #**39-write a Python Program to Sort the list according to the column using lambda
# array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# for i in range(len(array)):
#     sorted_array = sorted(array, key=lambda x: x[i])
#     print(f"Sorted array specific to column {i}, {sorted_array}")

# **40- write a program to Sort Python Dictionaries by Key or Value
# dic = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# # Sort dictionary by key
# sorted_dict = {k: dic[k] for k in sorted(dic)}
# print(f"Sorted dictionary by key: {sorted_dict}")
#
# # Sort dictionary by value
# sorted_dict = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
# print(f"Sorted dictionary by value: {sorted_dict}")

# #**41-write python program to Remove keys with Values Greater than K ( Including mixed values
# test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
# K = 7
# result_dict = {key: value for key, value in test_dict.items() if (isinstance(value, int) and value <= K) or (isinstance(value, str))}
# print(result_dict)

# **42-Write a Python program to concatenate the following dictionaries to create a new one
# dic1 = {1 : 10, 2 : 20}
# dic2 = {3 : 30, 4 : 40}
# dic3 = {5 : 50, 6 : 60}
#
# result_dic = {}
# result_dic.update(dic1)
# result_dic.update(dic2)
# result_dic.update(dic3)
# print(result_dic)

# **43-Write a Python program to iterate over dictionaries using for loops
# dic1 = {1 : 10, 2 : 20}
# for k in dic1:
#     print(k,":", dic1[k])

# **44- Write a Python script to merge two Python dictionaries
# dic1 = {1 : 10, 2 : 20}
# dic2 = {3 : 30, 4 : 40}
# result_dic = {}
# result_dic.update(dic1)
# result_dic.update(dic2)
# print(result_dic)

# **45-Write a Python program to get the maximum and minimum values of a dictionary values
# dic = {1: 3, 2: 30, 3: 44}
# print("the max value in this dictionary: ", max(dic.values()))
# print("the min value in this dictionary: ", min(dic.values()))

# **46- Write a Python program to drop empty items from a given dictionary.
# dic = {1: 3, 2: 33, 3: None}
# result_dic = {k: v for k, v in dic.items() if v is not None}
# print("Original dictionary:\n", dic)
# print("New dictionary after dropping empty items:\n", result_dic)

# **47-Write a Python program to create a tuple of numbers and print one item
# tpl = (1, 2, 3)
# print(tpl[0])

# # **48-Write a Python program to unpack a tuple into several variables
# tpl = ("taha", "ahmed", 20)
# first_name, last_name, age = tpl
# print("first name: ", first_name)
# print('last name: ', last_name)
# print("age: ", age)

# **49-Write a Python program to add an item to a tuple
# tpl1 = (1, 2, 3)
# item = 4
# tpl2 = tpl1 + (item,)
# print(tpl2)

# **50-Write a Python program to convert a tuple to a string
# tpl = ("apple", "banana", "orange")
# string = ','.join(tpl)
# print(string)

# **51-Write a Python program to convert a list to a tuple
# my_list = [1, 2, 3]
# my_list = tuple(my_list)
# print(my_list)

# **52-Write a Python program to reverse a tuple
# my_tuple = (1, 2, 3)
# reversed_tuple = my_tuple[::-1]
# print(reversed_tuple)

# **53-Write a Python program to replace the last value of tuples in a list.
# my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# val = 100
# new_list = [(*t[:-1], val) for t in my_list]
# print(new_list)

# **54-Write a Python program to convert a given string list to a tuple
# string = "python 3.0"
# my_list = []
# for i in string:
#     if i != " ":
#         my_list.append(i)
# my_tuple = tuple(my_list)
# print(my_tuple)

# **55-Write a Python program to calculate the average value of the numbers in a given tuple of tuples
# def calc_average(tpl):
#     some = 0
#     length = len(tpl)
#     for i in tpl:
#         some += i
#     return some/length
#
#
# my_tuple = (1, 2, 3, 4, 5)
# average = calc_average(my_tuple)
# print(average)

# **56-Write a Python program to add member(s) to a set.
# my_set = {1, 2, 3, 4}
# new_item = input()
# my_set.add(new_item)
# print(my_set)

# **57-Write a Python program to remove an item from a set if it is present in the set.
# my_set = {1, 2, 3, 4}
# deleted_item = int(input())
# my_set.discard(deleted_item)
# print(my_set)

# **58-Write a Python program to create an intersection,union,difference and symmetric difference of sets
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
#
# intersection = s1.intersection(s2)
# print("Intersection of s1 and s2: ", intersection)
#
# union = s1.union(s2)
# print("Union of s1 and s2: ", union)
#
# difference = s1.difference(s2)
# print("Difference of s1 and s2: ", difference)
#
# symmetric_difference = s1.symmetric_difference(s2)
# print("Symmetric difference of s1 and s2: ", symmetric_difference)

# **59-Write a Python program to find the maximum and minimum values in a set
# my_set = {1, 2, 3, 4}
# print("the min element in my set is: ", min(my_set))
# print("the max element in my set is: ", max(my_set))

# **60- Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
# my_list = [1, 2, 3, 4, 5, 8, 10]
# val = int(input())
# for i in range(0, len(my_list)):
#     for j in range(0, len(my_list)):
#         if my_list[i] + my_list[j] == val:
#             print(my_list[i], my_list[j])
