#! c:\Python3\python.exe
#############################################################################
import argparse
import os.path, time
import os, datetime
from os import path
#############################################################################
def Name(filename, directory):
	result = []
	print("Name")
	filename = filename + "."
	for root, dirs, files in os.walk(directory):
		for file in files:
			if filename in str(file):
				result.append(os.path.join(root, file))
	return result
#############################################################################
def Type(filetype, directory):
	result = []
	print("Type")
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith(filetype):
				result.append(os.path.join(root, file))
	return result
#############################################################################
def Date(date, directory, month, day, year):
	result = []
	print("Date")
	if month != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if month in str(dates):
						result.append(os.path.join(root, file))
				except:
					no_op = 0
	if day != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if day in str(dates):
						result.append(os.path.join(root, file))
				except:
					no_op = 0	
	if year != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if year in str(dates):
						result.append(os.path.join(root, file))
				except:
					no_op = 0	
	if date != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if date in str(dates):
						result.append(os.path.join(root, file))
				except:
					no_op = 0
	return result
#############################################################################
def NameType(filename, directory, filetype):
	result = []
	print("NameType")
	for root, dirs, files in os.walk(directory):
		for file in files:
			if filename in file:
				if filetype in file:
					result.append(os.path.join(root, file))
	return result
#############################################################################
def NameDate(filename, directory, date, month, day, year):
	result = []
	print("NameDate")
	if month != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if month in str(dates):
						if filename in str(files):
							result.append(os.path.join(root, file))
				except:
					no_op = 0
	if day != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if day in str(dates):
						if filename in str(files):
							result.append(os.path.join(root, file))
				except:
					no_op = 0	
	if year != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if year in str(dates):
						if filename in str(files):
							result.append(os.path.join(root, file))
				except:
					no_op = 0	
	if date != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if date in str(dates):
						if filename in str(files):
							result.append(os.path.join(root, file))
				except:
					no_op = 0
	return result
#############################################################################
def TypeDate(filetype, directory, date, month, day, year):
	result = []
	print("TypeDate")
	if month != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if month in str(dates):
						if file.endswith(filetype):
							result.append(os.path.join(root, file))
				except:
					no_op = 0
	if day != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if day in str(dates):
						if file.endswith(filetype):
							result.append(os.path.join(root, file))
				except:
					no_op = 0	
	if year != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if year in str(dates):
						if file.endswith(filetype):
							result.append(os.path.join(root, file))
				except:
					no_op = 0	
	if date != False:
		for root, dirs, files in os.walk(directory):
			for file in files:
				try:
					dates = time.strftime('%m/%d/%Y', time.localtime(os.path.getmtime((os.path.join(root, file)))))
					if date in str(dates):
						if file.endswith(filetype):
							result.append(os.path.join(root, file))
				except:
					no_op = 0
	return result
#############################################################################
def SaveCurrent (save, results):
	while os.path.exists(save + ".txt"):
		exists = input("this file has already been created, would you like to overwrite it? y/n: ")
		if exists == "y":
			break
		elif exists == "n":
			save = input("Please enter a new file name: ")
	with open(save + ".txt", "w") as f:
		for result in results:
			f.write('%s\n' % result)
	f.close()
##############################################################################
def SaveSpecified (specified, results):
	os.chdir(specified)
	while path.exists(specified) == False:
		specified = input("This directory does not exists please input a new path")
	
	name = input("Please choose a name for this file: ")
	while os.path.exists(name + ".txt"):
		exists = input("A file with this name already exists would you like to overwrite it? y/n: ")
		if exists == "y":
			break
		elif exists == "n": 
			name = input("Please enter a new name: ")
	with open(name + ".txt", "w") as f:
		for result in results:
			f.write('%s\n' % result)
	f.close()
##############################################################################
def Main():
	#parsing arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--path', help = "The path that you wish to search in. If there are spaces, be sure to put quotes around the path.", type = str, required = True)
	parser.add_argument('-n', '--filename', help = "The name of the file that you seek", type = str, default = False)
	parser.add_argument('-d', '--date', help = "The date that the file was last modified. MM/DD/YYYY", type = str, default = False)
	parser.add_argument('-t', '--filetype', help = "The type of file that you wish to find", type = str, default = False)
	parser.add_argument('-m', '--month', help = "The month the file was last modified in every findable year. MM", type = str, default = False)
	parser.add_argument('-a', '--day', help = "The day the file was last modified in every month and year. DD", type = str, default = False)
	parser.add_argument('-y', '--year', help = "Every file that was modified in chosen year. YYYY", type = str, default = False)
	parser.add_argument('-s', '--savecurrent', help = "This will save a .txt file to your current working directory, please choose a name for your file.", type = str, default = False)
	parser.add_argument('-e', '--savedir', help = "This will save a .txt file to the path of your choice, please specify the path you would like to save your file to.", type = str, default = False)
	args = parser.parse_args()
	#set arguments to easier variables
	directory = args.path
	filename = args.filename
	date = args.date
	filetype = args.filetype
	month = args.month
	day = args.day
	year = args.year
	save = args.savecurrent
	specified = args.savedir
	#checking if directory exists before proceeding
	while path.exists(directory) == False:
		directory = input("This directory you want to search in does not exist. Please input a new directory: ")
			
	if filename != False and date == False and filetype == False and month == False and day == False and year == False:
		#searching by filename
		results = Name(filename ,directory)
			
	if filename != False and filetype != False and date == False:
		#searching by filename and type
		results = NameType(filename ,directory, filetype)
			
	if date or month or day or year:
		if filename != False and filetype == False:
			#searching by filename and date
			results = NameDate(filename ,directory, date, month, day, year)

	if filetype and date == False and filename == False and month == False and day == False and year == False:
		#searching by filetype
		results = Type(filetype ,directory)

	if date != False or month != False or day != False or year != False:
		if filetype == False and filename == False:
			#searching by date
			results = Date(date ,directory, month, day, year)
			
	if date or month or day or year:
		if filetype != False and filename == False:
			#searching by date and filetype
			results = TypeDate(filetype ,directory, date, month, day, year)
	
	if save != False or specified != False:
		if save != False and specified == False:
			#save results to current directory if wanted by the user
			SaveCurrent(save, results)
		
		if specified != False and save == False:
			#save results to a specified directory if wanted by the user
			SaveSpecified(specified, results)
		 
	else:
		for r in results:
			print(r)		
#############################################################################		
Main()
#############################################################################
#search for files not folders add year at end of file for date