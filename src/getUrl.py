import os
# filename = "../blogUrl.txt"


def getUrl(filename):
	fid = open(filename, 'r+')
	lines = fid.readlines()

	print(type(lines))

	for line in lines:
		pass
	print(line)
	return line

# getUrl(filename)
