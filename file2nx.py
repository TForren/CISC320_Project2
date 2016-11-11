import networkx as nx
import sys

socialGraph = nx.MultiGraph()

f = open(sys.argv[1])
socialGraphFile = f.readlines()
f.close()

def parseFileLines(fileLines):
	splitLine = []
	testCaseCount = 0
	curTestCase = 1
	peopleCount = 0 #N
	linkCount = 0 #F
	partyCount = 0 #M
	partyHostCount = 0 #A
	partyHostIDs = [] 
	LP = 1 #Line Pointer skip first line

	testCaseCount = int(fileLines[0])
	print "loading", testCaseCount, "test cases..."
	while LP < len(fileLines):
		curLine = fileLines[LP]
		splitLine = curLine.split()
		
		if len(splitLine) == 4: #N, F, M, A
			peopleCount = int(splitLine[0])
			linkCount = int(splitLine[1])
			partyCount = int(splitLine[2])
			partyHostCount = int(splitLine[3])
			LP += 1
			print "Test case:",curTestCase
			print " People:", peopleCount
			print " Friendships:", linkCount
			print " Parties:", partyCount
			print " Hosts:", partyHostCount
			curTestCase += 1

		for lineNum in range(LP, linkCount+LP):
			curLine = fileLines[LP]
			splitLine = curLine.split()
			socialGraph.add_edge(splitLine[0],splitLine[1])
			print LP+1,"adding edge", splitLine[0],"and",splitLine[1]
			LP += 1
		
		if partyHostCount != 0:
			localPartyHosts = []
			for lineNum in range(LP,partyHostCount+LP):
				localPartyHosts.append(int(fileLines[lineNum]))
				LP += 1
			partyHostIDs.append(localPartyHosts)
			print "partyHostIDs:",partyHostIDs


parseFileLines(socialGraphFile)	
