# Complete the function below.
def insertCharacter(tempList, s):
	if not tempList:
		tempList.append(s)
	else:
		t = tempList[-1]
		while t > s and tempList:
			tempList.pop(-1)
			if tempList:
				t= tempList[-1]
		tempList.append(s)
	return tempList

def improbabilityCalculator(coordinates, remove):
	if remove >= len(coordinates):
		return "0"
	lengthCoordinates = len(coordinates)
	k = lengthCoordinates - remove
	tempList=[]
	res =""
	i = 0
	while i <= remove:
		tempList=insertCharacter(tempList, coordinates[i])
		i+=1
	while i < lengthCoordinates:
		res+=tempList[0]
		tempList.pop(0)
		tempList=insertCharacter(tempList, coordinates[i])
		i+=1
	res += tempList[0]
	tempList.pop(0)
	return res