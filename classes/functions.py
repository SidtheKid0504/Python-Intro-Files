# def myFunction(param):
#     print(param)

# myFunction('hello')

# myFile = open('test.txt', 'r')
# data = myFile.readlines()

# for i in data:
#     print(i)

# myString = 'dog, cat, bird, tree, fly cool'
# mySplit = myString.split(',')
# print(mySplit)

# def fileWordCount():
#     filename = input("Enter File Name: ")
#     inputFile = open(filename)

#     data = inputFile.read()
    
#     wordCount = len(data.split())
#     print(wordCount)

#     characterCount = 0
#     for i in data:
#         characterCount += 1
#     print(characterCount)

#     lineCount = len(data.split('\n'))
#     print(lineCount)

# fileWordCount()
    
# def factorialFinder(n):
#     return 1 if (n==1 or n==0) else n * factorialFinder(n - 1);

# print(factorialFinder(100))

# def findMaxNumber(num1, num2):
#     if num1 > num2:
#         print(f'{num1} is greater than {num2}')
#     elif num1 < num2:
#         print(f'{num2} is greater than {num1}')
#     else:
#         print(f'{num1} is equal to {num2}')

# findMaxNumber(1, 5)

# def findPrime(num):
#     print(num)
#     if num == 1:
#         print('Number Is Not Prime')
#     elif  num % 2 == 0 or num % 3 == 0:
#         print('Number is Not Prime')
#         i = 5
#         while i <= num:
#             if num % i == 0 or num % i + 2 == 0:
#                 print('Number is Not Prime')
#                 i += 1
#     else:
#         print('Number is Prime')
# findPrime(11)

# dictionary = {'key1': 'value1',  'key2': 'value2', 'key3': ['value3', 'value3.5'], 'key4': 'value4'}
# print(dictionary['key3'])