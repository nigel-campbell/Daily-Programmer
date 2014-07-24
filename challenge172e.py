# Daily Programmer Challenge #172 (www.reddit.com/r/dailyprogrammer)

# Challenge Description:

# A portable bitmap is one of the oldest image formats around and grants access to very simple image creation and sharing.
# Today, you will be creating an image of this format.
# A simple PBM program can be seen here[1] (Note that we'll be creating the simplest version, a PBM, not PPM or PGM.)
# But basically the program consists of the following:
# A 2byte string (usually 'P1') denoting the file format for that PBM
# 2 integers denoting the Width and Height of our image file respectively
# And finally, our pixel data - Whether a pixel is 1 - Black or 0 - White.

# See link for details:
# http://www.reddit.com/r/dailyprogrammer/comments/2ba3g3/7212014_challenge_172_easy/

def mapFileToDict():
	letterMappings = {}
	fileName = 'TestFolder/font.txt'
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

def constructOutput(mappings, inputString):
	inputString = inputString.upper()
	output = ''
	for num in range(0,8):
		for char in inputString:
			if char == ' ':
				continue
			currentMap = mappings[char]
			output += getLineFromString(num, currentMap)
		output += '\n'
	return output

def writeStringToPBM(output, fileName):
	f = open('Test Folder/' + fileName + '.pbm', 'w')
	f.write(output)
	f.close()

def main():
	mapping = mapFileToDict()
	word = raw_input("Enter word of phrase: ")
	output = constructOutput(mapping, word)
	fileName = raw_input("Enter output file name: ")
	writeStringToPBM(output, fileName)

if __name__ == '__main__':
	main()
	pass