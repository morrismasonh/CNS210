<<<<<<< HEAD
import os
import argparse

#Fibonacci function
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

#asks for a file name from the user
print("Please note that the file will be saved in your current working directory")
FileName = input("Please input the file name: ")
#checks if the file exists in the current path, and will ask the user if they want to overwrite the existing file.
while os.path.exists(FileName + ".txt"):
    exists = input("This file already exists. Do you want to overwrite it? (y/n): ")
    if exists == "y" or exists == "yes" or exists == "Y" or exists == "Yes" or exists == "YES":
        break
    elif exists == "n" or exists == "no" or exists == "N" or exists == "No" or exists == "NO":
        FileName = input("Please input a new file name: ")
#Creates file if file dosent already exist or if user wants it to be overwritten
f = open(FileName + ".txt", "w")

#ask user for fibonacci number input
num = int(input("Please enter a number: "))

#prints the result, stores it in created file ,tells user where the file is located, and closes the file
print("The Fibonacci number is: " + str(fib(num)))
f.write("The Fibonacci number is: " + str(fib(num)))
cwd = os.getcwd()
print("Results saved in " + cwd + ": " + FileName + ".txt")
=======
import os
import argparse

#Fibonacci function
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

#asks for a file name from the user
print("Please note that the file will be saved in your current working directory")
FileName = input("Please input the file name: ")
#checks if the file exists in the current path, and will ask the user if they want to overwrite the existing file.
while os.path.exists(FileName + ".txt"):
    exists = input("This file already exists. Do you want to overwrite it? (y/n): ")
    if exists == "y" or exists == "yes" or exists == "Y" or exists == "Yes" or exists == "YES":
        break
    elif exists == "n" or exists == "no" or exists == "N" or exists == "No" or exists == "NO":
        FileName = input("Please input a new file name: ")
#Creates file if file dosent already exist or if user wants it to be overwritten
f = open(FileName + ".txt", "w")

#ask user for fibonacci number input
num = int(input("Please enter a number: "))

#prints the result, stores it in created file ,tells user where the file is located, and closes the file
print("The Fibonacci number is: " + str(fib(num)))
f.write("The Fibonacci number is: " + str(fib(num)))
cwd = os.getcwd()
print("Results saved in " + cwd + ": " + FileName + ".txt")
>>>>>>> 9acf5ce7d04c91eaa3412542adfadcd23609f1f1
f.close()