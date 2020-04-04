import os
import argparse

#Fibonacci module that calculates the fibonacci number
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
        
def Main():
    parser = argparse.ArgumentParser()
    #argument for the fibonacci number
    parser.add_argument("num", help = "The Fibonacci number you wish to calculate", type = int, default = True)
    #argument for the file name that is going to be created
    parser.add_argument("name", help = "The filename you wish to name the created file", type = str, default = True)
    args = parser.parse_args()
    
    #calculates results and assigns it to results
    results = fib(args.num)
    #assigns the inputed filename to FileName
    FileName = (args.name)
    
    #loop to check if the file exists and asks the user if they want to overwrite it if it does
    while os.path.exists(FileName + ".txt"):
        exists = input("This file already exists. Do you want to overwrite it? (y/n): ")
        if exists == "y" or exists == "yes" or exists == "Y" or exists == "Yes" or exists == "YES":
            break
        elif exists == "n" or exists == "no" or exists == "N" or exists == "No" or exists == "NO":
            FileName = input("Please input a new file name: ")
    #Creates file if file dosent already exist or if user wants it to be overwritten
    f = open(FileName + ".txt", "w")

    #prints the result, stores it in created file ,tells user where the file is located, and closes the file
    print("The Fibonacci number is: " + str(results))
    f.write("The Fibonacci number is: " + str(results))
    cwd = os.getcwd()
    print("Results saved in " + cwd + ": " + FileName + ".txt")
    f.close()

Main()