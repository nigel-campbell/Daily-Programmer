# Daily Programmer Challenge #166b (www.reddit.com/r/dailyprogrammer)

# Challenge Description:  

# Every time you send or receive data across the internet, 
# it has navigated itself through tens or hundreds of intermediate 
# destinations to finally reach its target. This involves a ton 
# of extremely well optimised algorithms to find the fastest way 
# to get from A to B - and all of this happens without you knowing 
# about it - until now. The network engineers at Notfast Internet
# have detected a problem with a central node - it's not letting 
# any packets through! They are hiring some engineers to manually
# route the packets while they go about fixing the problem.

# Challenge Details: 

# You are given a distance Matrix[2] (which we met back in
# April[3] - go check out that for a more in depth discussion of graphs) 
# to represent the portion of the network you are dealing with. The pings 
# between nodes on the network will all be different, and it is the 
# job of your algorithm to account for this. Your job and challenge
# will be to write a program that will find the route through the network
#  from one node to another that has the shortest ping.

# See link for additional details: 
# http://www.reddit.com/r/dailyprogrammer/comments/287jxh/6152014_challenge_166b_hard_a_day_in_the_life_of/
import heapq

def transformToMatrix(filePath):
	matrix = {}
	start, end = '',''
	with open(filePath) as fileObj:
		size = int(fileObj.readline())
		for num in range(size):
			currentLine = fileObj.readline()
			listOfAdjacencyValues = currentLine.split(',')
			matrix[num] = listOfAdjacencyValues
		lastLine = fileObj.readline()
		start, end = lastLine.split()[0], lastLine.split()[1]
	return matrix, start, end, size

def getLetter(num):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if (num >= 0 and num < 26):
		return alphabet[num]
	else:
		raise Exception("Outside of the alphabet")

def getIndex(letter):
	if(len(letter) > 1):
		raise Exception("Letter, not word")
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	count = 0
	for letterVar in alphabet:
		if letterVar == letter:
			break
		count += 1
	return count

def dijkstrasAlgorithm(matrix, start, end, size):
	queue = []; currentPath = start; shortestPathDistance = 0;
	currentNode = (shortestPathDistance, start, currentPath)
	heapq.heappush( queue, currentNode )

	while (len(queue) != 0):
		currentNode = heapq.heappop(queue)
		currentLetter = str(currentNode[1])
		visitedNodes = currentNode[2]
		adjacencies = matrix[getIndex(currentLetter)]	
		if currentLetter == end:
			break
		count = 0
		for distance in adjacencies:
			if int(distance) != -1:
				nodeID = getLetter(count)
				if(nodeID in visitedNodes):
					count+=1
					continue
				newPath = visitedNodes + nodeID
				newDistance = currentNode[0] + int(distance)
				newItemForQueue = (newDistance, nodeID, newPath)
				heapq.heappush(queue, newItemForQueue)
			count+=1
	print "Shortest Path: " + str(currentNode)
	return currentNode

def main():
	filePath = 'TestFolder/input1Challenge166bh.txt'
	matrix, start, end, size = transformToMatrix(filePath)
	print dijkstrasAlgorithm(matrix,start,end,size)


if __name__ =="__main__":
	main()