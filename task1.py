import os

def printfiles(files):
	for name in os.listdir(files):
		path = os.path.join(files,name)
		if os.path.isfile(path):	
			print(path)

printfiles('.')

