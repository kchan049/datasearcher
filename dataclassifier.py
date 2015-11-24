#!/usr/bin/env python

import time
import re
import sys, os, traceback, optparse
import struct

def main():
	largedataset = []
	smalldataset = []
	get_decimals_from_file("cs_170_small4.txt", smalldataset)

def get_decimals_from_file(file_name, dataset):
	file = open(file_name)
	for i in file:
		strdecimal = file.readline().split()
		dataset.append(list(map(float,strdecimal)))
	for i in dataset:
		print(i)
	
	#strdecimal = file.readline().split()
	#return map(float, strdecimal)
if __name__ == '__main__':
	sys.exit(main())
