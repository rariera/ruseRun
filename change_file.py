#!/usr/bin/env python3

import fileinput

tempFile = open("test.txt", "r")
old = tempFile.read()
other = open('notes.txt', 'w')

for line in old:
	print(line)
	for char in line:
		if char != ' ':
			line.replace(char, '#')
	other.write(line)
	print(line)
tempFile.close()
other.close()

