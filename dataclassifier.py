#!/usr/bin/env python

import time
import re
import sys, os, traceback, optparse
import struct
import os.path

def main():
	largedataset = [] #list to store the largedataset
	smalldataset = [] #list to store the smalldataset
	data = []
	print("Welcome to Kenneth Chan's Feature Selection Algorithm\n") #welcomes user
	filename = input("Type in the name of the file to test: ")	#takes in file
	if os.path.isfile(filename) == False : # checks if file exists
		sys.exit(main()) 
	algo_number = input("Type the number of the algorithm you want to run.\n") #which algo does user want to use
	if "small" in filename:
		get_decimals_from_file(filename, smalldataset) #takes in smalldataset and converts from scientific to decimal
		data = smalldataset
	if "big" in filename:
		get_decimals_from_file(filename, largedataset)
		data = largedataset
	print('This dataset has {} features (not including the class attribute), with {} instances\n'.format( len(data[0])-1, len(data)))
	print("Please wait while I normalize the data...  Done!")
#this function takes in a file name and converts from scientific to decimal and also organizes the dataset into each class set
def get_decimals_from_file(file_name, dataset):
	file = open(file_name)
	for i in file:
		strdecimal = i.split()
		dataset.append(list(map(float,strdecimal)))
	for i in dataset:
		print(i)
	
	#strdecimal = file.readline().split()
	#return map(float, strdecimal)

if __name__ == '__main__':
	sys.exit(main())
