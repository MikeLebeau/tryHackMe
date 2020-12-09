import os

# read all file in decom 2 and find the file with 'password'
ListFile = os.listdir('decom2')
for l in ListFile:
	f = open('decom2/' + l,'r', encoding="utf-8",errors='ignore')
	data = f.read()
	f.close()
	
	if "password" in data:
		print(l)
