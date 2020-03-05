# f = open("newdocument.txt","w")
# f.write("Free Automation Testing Tutorials \n  courses on Selenium, appium, jenkins, docker, kubernetes, jmeter, git, githuh, postman, soapui, api testing, ui testing, ci, ... \n You visited this page on 5/2/20.")
# f.close()
# print("file has been created")
#
# r = open("newdocument.txt","r")
# data = r.read()
# print(data)
# r.close()
#
# print("\n \n \n \n")
# try:
#     r = open("newdocument.txt", "r")
#     data = r.read()
#     print(data)
#     f.close()
# # except IOError as a:
# #     print("operations faile: ", a)
# #
# #
# # f = open("newdocument.txt","a")
# # f.write("ASASASASASASASASASAS \n  ")
# # f.close()
# # print("file has been created")
#
#
# def reverse(s):
#     str = ""
#     print(len(s))
#     for i in s:
#         str = i + str
#         # print(str)
#     return str
#
#
# # # s = "Geeksforgeeks"
# # s = input("Enter String: ")
# # print("The original string  is : ", end="")
# # print(s)
# #
# # print("The reversed string(using loops) is : ", end="")
# #
# # output_Str = reverse(s)
# #
# # print("Data Structures \n")
#
# output_Str = "Automation"
#
# print(output_Str)
# print("O/P of Lower case: ",output_Str.lower())
# print("O/P of Upper case: ",output_Str.upper())
# print("O/P of Capitalize: ",output_Str.capitalize())
# print("O/P of stip: ",output_Str.strip())
# print("O/P of Lstip: ",output_Str.lstrip("a"))
# print("O/P of Rstip: ",output_Str.rstrip("a"))
# print("O/P of Split: ",output_Str.split("a"))
# print("O/P of Is Alpha: ",output_Str.isalpha())
# print("O/P of Replace: ",output_Str.replace("a","auto"))
# print("O/P of ASCII: ",output_Str.isascii())
#
# print(ascii(output_Str))

#
# str="my name is subbareddy"
#
# index = str.index("is")
# print("Index Value of 'Is': ",index)
#
# t=tuple(str)
# print(t)
# print(t.index('r'))
#
#
#
#
#
# # vowels list
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# # index of 'e'
# index = vowels.index('e')
# print('The index of e:', index)
# # index of the first 'i'
# index = vowels.index('i')
# print('The index of i:', index)
#
#
# str = "testing"
# index = str.index("i")
# print("index of t: ",index)
#
#
#
# # word=str.split()
# # for i in word:
# #     print(i)
# # print(word)

# problem:Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


# str = int(input("Enter Integer: "))
#
# if str % 2 ==0:
#     print("Weird")
# else:
#     if str >=2 and str <= 5:
#         print("Not Weird")
#     elif str >= 6 and str <=20:
#         print("Weired")
#     elif str >=20:
#         print("Not Weird")

# Enter Integer: 3
# Not Weird
# Enter Integer: 4
# Weird

# Enter Integer: 7
# Weired

# Enter Integer: 30
# Weird


# def convertOpposite(str):
#     ln = len(str)
#
#     # Conversion according to ASCII values
#     for i in range(ln):
#         if str[i] >= 'a' and str[i] <= 'z':
#
#             # Convert lowercase to uppercase
#             str[i] = chr(ord(str[i]) - 32)
#
#         elif str[i] >= 'A' and str[i] <= 'Z':
#
#             # Convert lowercase to uppercase
#             str[i] = chr(ord(str[i]) + 32)
#
#         # Driver code
#
#
# if __name__ == "__main__":
#     str = "GeEkSfOrGeEkS"
#     str = list(str)
#
#     # Calling the Function
#     convertOpposite(str)
#
#     str = ''.join(str)
#     print(str)

# def convertOpposite(str):
#     ln = len(str)
#
#     for i in range(ln):
#
#         if str[i] >= 'a' and str[i] <= 'z':
#            # Convert lowercase to uppercase
#             str[i] = chr(ord(str[i]) - 32)
#             # print("Upper case :",str[i])
#         elif str[i] >= 'A' and str[i] <= 'Z':
#             # Convert lowercase to uppercase
#             str[i] = chr(ord(str[i]) + 32)
#             # print("lower case :",str[i])
#         # Driver code
#
#
# if __name__ == "__main__":
#     str = "cHaNdRaSeKhAr"
#     str = list(str)
#
#     # Calling the Function
#     convertOpposite(str)
#
#     str = ''.join(str)
#     print(str)
#
#
# print("ASCII: ", ord("a"))
# print("ASCII: ", ord("b"))
# print("ASCII: ", ord("c"))
# print("ASCII: ", ord("d"))
# # print("ASCII: ", ord("e"))
# dict = {}

#
# def printDuplicates(arr):
#     dict = {}
#
#     for ele in arr:
#         try:
#             dict[ele] += 1
#         except:
#             dict[ele] = 1
#
#     for item in dict:
#
#         # if frequency is more than 1
#         # print the element
#         if (dict[item] > 1):
#             print(item, end=" ")
#
#     print("\n")
#
#
# # Driver Code
# if __name__ == "__main__":
#     list = [12, 11, 40, 12,5, 6, 5, 12, 11]
#     printDuplicates(list)


# dicvalue = {'val1':1,'val2':2,'val3':3,1:[1,2,3,4]}
# keyval = dicvalue.keys()
# valValue = dicvalue.values()
# print(keyval)
# print(dicvalue.items())


# #Creating an empty Tuple
# Tuple1 = ()
# print("Initial empty Tuple: ")
# print (Tuple1)
#
# #Creatting a Tuple
# #with the use of string
# Tuple1 = ('Geeks', 'For')
# print("\nTuple with the use of String: ")
# print(Tuple1)

# Creating a Tuple with
# the use of list
# list1 = [1, 2, 4, 5, 6]
# print("\nTuple using List: ")
# print(tuple(list1))
#
# #Creating a Tuple
# #with the use of built-in function
# Tuple1 = tuple('Geeks')
# print("\nTuple with the use of function: ")
# print(Tuple1)
#
# newtuple1 = tuple('chandra')
# print(newtuple1)
#
# Tuple1 = (0, 1, 2, 3,4,5,6,7)
# Tuple2 = ('python', 'geeks')
# Tuple3 = (Tuple1, Tuple2)
# print("\nTuple with nested tuples: ")
# print(Tuple3)
#
#
# set1 = set(["Geeks", "For", "Geeks"])
# print("\nSet with the use of List: ")
# print(set1)
#

# set1 = set()
#
# set1.add(1)
# set1.add(2)
# print(set1)
#
# for i in range(1,10):
#     set1.add(i)
# print(set1)
# set1.update([10,11,12])
# print(set1)
#
# for i in range(1, 5):
#     set1.remove(i)
# print("\nSet after Removing a range of elements: ")
# print(set1)
#
# set1.remove(6)
# print(set1)
# set1.discard(7)
# print(set1)
#
# set2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# for i in range(1, 5):
#     set2.remove(i)
# print("\nSet after Removing a range of elements with revmove: ")
# print(set2)
# set2.clear()
# print(set2)


# Python program to demonstrate
# Adding Elements to a Array
#
# # importing "array" for array creations
# import array as arr
#
# # array with int type
# a = arr.array('i', [1, 2, 3])
#
# print("Array before insertion : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()
#
# # inserting array using
# # insert() function
# a.insert(1, 4)
#
# print("Array after insertion : ", end=" ")
# for i in (a):
#     print(i, end=" ")
# print()
#
# # array with float type
# b = arr.array('d', [2.5, 3.2, 3.3])
#
# print("Array before insertion : ", end=" ")
# for i in range(0, 3):
#     print(b[i], end=" ")
# print()
#
# # adding an element using append()
# b.append(4.4)
#
# print("Array after insertion : ", end=" ")
# for i in (b):
#     print(i, end=" ")
# print()
#
#
#

#
# import array as arr
#
# a = arr.array('i', [1,2,3])
#
# print("Before print:", end =" ")
# for i in range(0,3):
#     print(a[i], end=" ")
# print()
#
# a.insert(1,4)
# print(a)
# print("Before print:", end =" ")
# for i in range(0,4):
#     print(a[i], end=" ")
# print()
#
# with open("chandra.txt","w") as f_handling:
#     f_handling.write("Helloooooooooooooooooooooooooo")
# print(f_handling.closed)

# f = open("chandra.txt","r")
# # print(f.read())
# print(f.read(5))
# f.seek(0)
# print(f.read(100))
# f.close()
# print("Print completed ")


# # Python code to illustrate split() function
# with open("chandra.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split('l')
#         print(word)


# Module Regular Expression is imported using __import__().
# import re
#
# # compile() creates regular expression character class [a-e],
# # which is equivalent to [abcde].
# # class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
# p = re.compile('[a-z]')
#
# # findall() searches for the Regular Expression and return a list upon finding
# print(p.findall("Aye, said Mr. Gibenson Stark"))
#
#
# import re
#
# # '*' replaces the no. of occurrence of a character.
# p = re.compile('ab*')
# print(p.findall("ababbaabbbabababababababbbbab"))

# # Reading an excel file using Python
# import xlrd
#
# # Give the location of the file
# loc = ("path of file")
#
# # To open Workbook
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# # For row 0 and column 0
# sheet.cell_value(0, 0)


# f1 = open("newdocument.txt","r")
# f2 = open("chandra.txt","w")
#
# for x in f1:
#     print(x)
#     f2.write(x)
#
# f1.close()
# f2.close()

#import os

# os.mkdir("chandra")
# os.chdir("chandra")
# print(os.getcwd())
# print("Done")
#
# os.rmdir("chandra")


# with open("chanadra.txt","r+") as fr:
#     fr.write(" ")
#     fr.write("testtestsetesttesttestsetesttesttestsetesttesttestsetesttesttestsetesttesttestsetest")
#     print(fr.readlines())
#     print(fr.tell())
# print(fr.closed)



























