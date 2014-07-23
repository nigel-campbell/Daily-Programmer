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

def getLineFromString(lineNumber, string):
	line = ''
	currentLine = 0
	for char in string:
		if char == '\n':
			currentLine += 1
			continue
		if currentLine == lineNumber:
			line+=char
		if currentLine != lineNumber:
			continue
	line += ' '
	return line

def constructOutput():
	inputString = inputString.upper()
	output = ''
	
def writeStringToPBM():
	pass
def main():
	pass