# Daily Programmer Challenge #167m (www.reddit.com/r/dailyprogrammer)

# Challenge Description: 

# It is that time of year again. The Intro to Computer Science 101 
# class has ended at Greendale community college and the professor 
# has to submit the final grades. The school requires grades to be 
# submitted with a letter grade. In addition the grades should be 
# submitted from the "best" student first. The individual scores 
# should be be listed from "worse" to "best".

# Challenge Details:

# The output should be ranked from the "best" student who had the best 
# grade to the "worse" student who had the lowest grade. The 5 scores
# should also be arranged from the "lowest" to "highest".
# The output should take on this form:
# (Last Name) (First Name) (Final percentage) (Final Grade) : (Scores 1-5 from low to high)

# See link for details:
# http://www.reddit.com/r/dailyprogrammer/comments/28gq9b/6182014_challenge_167_intermediate_final_grades/

import re

def interpretLine(line):
	name = ''; grades = [];
	namePattern = '[A-Z][a-z]+'; gradePattern = '[0-9][0-9]*';
	for item in line:
		if re.match(namePattern, item):
			if len(name) == 0:
				name = name + item
			else: 
				name = name + ' ' + item
		elif re.match(gradePattern, item):
			grades.append(item)
	grades = map(int, grades); grades.sort();
	return name, grades

def readinput(filePath):
	gradebook = {}
	with open(filePath) as inputFile:
		for line in inputFile:
			splitLine = line.split()
			key, content = interpretLine(splitLine)
			gradebook[key] = content
	return gradebook

def calculateLetterGrade(grade):
	letter = ''

	if grade > 93: letter = 'A'
	elif grade > 90: letter = 'A-'
	elif grade > 87: letter = 'B+'
	elif grade > 83: letter = 'B'
	elif grade > 80: letter = 'B-'
	elif grade > 77: letter = 'C+'
	elif grade > 73: letter = 'C'
	elif grade > 70: letter = 'C-'
	elif grade > 67: letter = 'D+'
	elif grade > 63: letter = 'D'
	elif grade > 60: letter = 'D-'
	else: letter = 'F'

	return letter

def computeFinalAverages(gradebook):
	finalAverages = []
	for student in gradebook:
		studentInfo = (student, gradebook[student])
		finalAverage = sum( studentInfo[1] ) / float( len(studentInfo[1]) )
		finalLetterGrade = calculateLetterGrade(finalAverage)
		finalAverages.append( (studentInfo, finalAverage, finalLetterGrade) )
	finalAverages.sort( key=lambda final: final[1], reverse = True )
	return finalAverages

def printOutputToFile(finalAverages, writePath):
	with open(writePath, "w") as newFile:
		for student in finalAverages:
			string = ""
			string += str(student[0][0]) # Name
			string += ' (' + str( student[1]) + '%)' # Average
			string += ' (' + str( student[2]) + ')' # Letter
			string += ': ' + str( student[0][1] ) # Grades
			newFile.write(string + '\n')

def main():
	filePath1 = 'TestFolder/input1Challenge167m.txt'
	filePath2 = 'TestFolder/input2Challenge167m.txt'
	outputFile = 'TestFolder/resultsChallenge167m.txt'
	printOutputToFile(computeFinalAverages(readinput(filePath1)), outputFile)

if __name__=="__main__":
	main()