def mapFileToDict():
	letterMappings = {}
	fileName = 'font.txt'
	currentLetter = 'A'
	currentMapping = ''
	with open(fileName) as fontMappings:
		for line in fontMappings:
			if len(line) == 2:
				if len(currentMapping) != 0: 
					letterMappings[currentLetter] = currentMapping
					currentMapping = ''
				currentLetter = line[0]
			else:
				currentMapping += ('0 ' + line)
	return letterMappings

def getLineFromString():
	pass
def constructOutput():
	pass
def writeStringToPBM():
	pass
def main():
	pass