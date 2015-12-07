#!/usr/bin/env python
import math
import time
import re
import sys, os, traceback, optparse
import struct
import os.path
import numpy

def main():
	largedataset = [] #list to store the largedataset
	smalldataset = [] #list to store the smalldataset
	data = []
	print("Welcome to Kenneth Chan's Feature Selection Algorithm\n") #welcomes user
	filename = input("Type in the name of the file to test: ")	#takes in file
	if os.path.isfile(filename) == False : # checks if file exists
		sys.exit(main()) 
	algo_number = input("Type the number of the algorithm you want to run.\n1. forward\n2. backward\n3. custom") #which algo does user want to use
	if "small" in filename:
		get_decimals_from_file(filename, smalldataset) #takes in smalldataset and converts from scientific to decimal
		data = smalldataset
	if "big" in filename:
		get_decimals_from_file(filename, largedataset)
		data = largedataset
	print('This dataset has {} features (not including the class attribute), with {} instances\n'.format( len(data[0])-1 , len(data)))
	print("Please wait while I normalize the data...")

#	col = 1
#	for col in range(len(data[0])):
#		storage = []
#		for row in range(len(data)):
#			storage.append(data[row][col])
#		storage = normalize(storage)
#		for row in range(len(data)):
#			data[row][col] = storage[row]
	print("Done !")
	if(algo_number == "1"):
		forwardselection(data)	
	elif algo_number == "2":
		backwardselection(data)
	else:
		customforwardselection(data)
#the following function is based off of the slides project briefing 
def forwardselection(data):
	highaccuracy = 0
	chooseset = [] #this is the set where we store the highest accuracy features
	currentset = [] 
	row = 1
	#in backwards we add all of the features intially
	#for forwards we start out initially with no features and keep adding
	for row in range(len(data[0])):
		best = 0
		wrong = 0
		j = 1
		featuretoadd = 0
		for j in range(len(data[0])):
			if j not in currentset and j != 0:
				intersection = []
				currentfeat = []
				currentfeat.append(j)
				currentset.sort()
				print("Using features ")
				currentset.append(j)
				#i = 0
				#for i in range(len(currentset)):
				#		print("{} ".format(currentset[i]))
				print(currentset)
				accuracy = validation(data,currentset,j,wrong)
				
				currentset.remove(j)
				print("accuracy is {} \n".format(accuracy))
				#print("accu:", accuracy, "bst", best)
				if accuracy > best:
					best = accuracy
					featuretoadd = j
		#here we add feature to add to the current set
		currentset.append(featuretoadd)
		print("Feature Set")
		print(currentset)
		#for i in range(len(currentset)):
		#		print("{} ".format(currentset[i]))
		print(" was the best, and the accuracy is {}\n".format(best))
		highaccuracy = max(highaccuracy, best)
		if highaccuracy == best:
			chooseset = []
			chooseset += currentset
	print("Finished! The best feature(s) is")
	print( chooseset)
	#for i in range(len(chooseset)):
	#		print("{} ".format(chooseset[i]))
	print(" which has an accuracy of {} \n".format(highaccuracy))

def customforwardselection(data):
	highaccuracy = 0
	chooseset = [] #this is the set where we store the highest accuracy features
	currentset = [] 
	row = 1
	#in backwards we add all of the features intially
	#for forwards we start out initially with no features and keep adding
	for row in range(len(data[0])):
		best = 0
		wrong = sys.maxsize
		j = 1
		featuretoadd = 0
		for j in range(len(data[0])):
			if j not in currentset and j != 0:
				intersection = []
				currentfeat = []
				currentfeat.append(j)
				currentset.sort()
				print("Using features ")
				currentset.append(j)
				#i = 0
				#for i in range(len(currentset)):
				#		print("{} ".format(currentset[i]))
				print(currentset)
				accuracy = customvalidation(data,currentset,j,wrong)
				
				currentset.remove(j)
				print("accuracy is {} \n".format(accuracy))
				#print("accu:", accuracy, "bst", best)
				if accuracy > best:
					best = accuracy
					featuretoadd = j
		#here we add feature to add to the current set
		currentset.append(featuretoadd)
		print("Feature Set")
		print(currentset)
		#for i in range(len(currentset)):
		#		print("{} ".format(currentset[i]))
		print(" was the best, and the accuracy is {}\n".format(best))
		highaccuracy = max(highaccuracy, best)
		if highaccuracy == best:
			chooseset = []
			chooseset += currentset
	print("Finished! The best feature(s) is")
	print( chooseset)
	#for i in range(len(chooseset)):
	#		print("{} ".format(chooseset[i]))
	print(" which has an accuracy of {} \n".format(highaccuracy))



def backwardselection(data):
	highaccuracy = 0
	chooseset = []
	currentset = []
	for i in range(len(data[0])): #we add all the features then later in the process we remove the features to add
		currentset.append(i)
	row = 1
	for row in range(len(data[0])):
		best = 0
		wrong = 0 #the number of wrong is for the custom algorithm 
		j = 1
		featuretoadd = 0
		for j in range(len(data[0])):
			if j not in currentset and j != 0:
				intersection = []
				currentfeat = []
				currentfeat.append(j)
				currentset.sort()
				print("Using features ")
				currentset.append(j)
				#i = 0
				#for i in range(len(currentset)):
				#		print("{} ".format(currentset[i]))
				print(currentset)
				accuracy = validation(data,currentset,j,wrong)
				
				currentset.remove(j) #we append and remove j from currentset just to get the accuracy
				print("accuracy is {} \n".format(accuracy))
				#print("accu:", accuracy, "bst", best)
				if accuracy > best: #compare the accuracy to the previous best accuracy
					best = accuracy
					featuretoadd = j
		currentset.pop(currentset.index(featuretoadd)) #for backwards we pop instead of append the feature to add
		print("Feature Set")
		print(currentset)
		#for i in range(len(currentset)):
		#		print("{} ".format(currentset[i]))
		print(" was the best, and the accuracy is {}\n".format(best))
		highaccuracy = max(highaccuracy, best) #takes the best accuracy
		if highaccuracy == best:
			chooseset = []
			chooseset += currentset
	print("Finished! The best feature(s) is")
	print( chooseset)
	#for i in range(len(chooseset)):
	#		print("{} ".format(chooseset[i]))
	print(" which has an accuracy of {} \n".format(highaccuracy))


		
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
#this function normalizes the data (x-mean(set))/stdev(set)
def normalize(dataset):
	row = 0
	for col in dataset:
		dataset[row] = (dataset[row]-numpy.mean(dataset))/numpy.std(dataset)
		row = row +1		
	return dataset		
#this function uses leave one out validation
def validation(data, currentset, x, wrong):
	data.append(x)
	correct = 0
	for row in range(len(data) - 1):
		dist = 0
		nearest = sys.maxsize
		index = 0
		for col in range(len(data) - 1):
			if row is not col:
				dist = 0
				#uses distance function
				for i in currentset:
					dist += (data[row][i] - data[col][i]) ** 2
				dist = math.sqrt(dist)
				#takes the minimum of the nearest neighbor and distance
				nearest = min(nearest, dist)
				if nearest == dist:
					index = row
					index1 = col
		if data[index][0] == data[index1][0]:
			correct += 1 #we increment the number of correct instances
	data.remove(x)
	return correct/len(data)
def customvalidation(data, currentset, x, wrong):
	data.append(x)
	correct = 0
	wrongs = 0
	for row in range(len(data) - 1):
		dist = 0
		nearest = sys.maxsize
		index = 0
		for col in range(len(data) - 1):
			if row is not col:
				dist = 0
				#uses distance function
				for i in currentset:
					dist += (data[row][i] - data[col][i]) ** 2
				dist = math.sqrt(dist)
				#takes the minimum of the nearest neighbor and distance
				nearest = min(nearest, dist)
				if nearest == dist:
					index = row
					index1 = col
		if data[index][0] == data[index1][0]:
			correct += 1 #we increment the number of correct instances
		wrongs += 1
		if wrongs > wrong:
			return 0
	data.remove(x)
	return correct/len(data)



if __name__ == '__main__':
	sys.exit(main())
