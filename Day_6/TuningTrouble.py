tempInput = open("input.txt", "r").read()

for i in range(len(tempInput)):
	if(len(set(tempInput[i:i+4])) == 4):
		print("Solution 1:", i+4)
		break

for i in range(len(tempInput)):
	if(len(set(tempInput[i:i+14])) == 14):
		print("Solution 2:", i+14)
		break