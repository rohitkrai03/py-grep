import re
import os

def convert_patterns(patterns):
	results = []

	# for each pattern
	for pattern in patterns:
		# make a regular expression with it
		expr = re.compile(pattern)
		results.append(expr)
	# return the results
	return results

def troll_directories(start):
	# troll for all the directories like in find
	results = []
	# Traverse the directory for all the files.
	for root, dirs, files in os.walk(start):
		for fname in files:
			# put the full path into the results
			results.append(os.path.join(root, fname))
	return results

def apply_patterns(files, patterns):
	# for each file in files
	for fname in files:
		# open the file and read the lines
		lines = open(fname).readlines()
		for num, line in enumerate(lines):
			# for each pattern
			for pattern in patterns:
				# if pattern found in contents
				if pattern.search(lines):
					# print file, line number, line
					print("{}:{}:   {}".format(os.path.join(fname), num+1, line))