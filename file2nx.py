import networkx as nx
import sys
import partyCalcs as pc

#socialGraph = nx.Graph()
#parser output contains Graph, partyCount, hostCount
#parserOutput = []
f = open(sys.argv[1])
socialGraphFile = f.readlines()
f.close()
DEBUG = False

parserOutput = []
def parseFileLines(fileLines):
	socialGraph = nx.Graph()
	splitLine = []
	testCaseCount = 0
	curTestCase = 0
	peopleCount = 0 #N
	linkCount = 0 #F
	partyCount = 0 #M
	partyHostCount = 0 #A
	partyHostIDs = []
	LP = 1 #Line Pointer skip first line

	testCaseCount = int(fileLines[0])
	if DEBUG:
		print "Processing", testCaseCount, "test cases..."
	while LP < len(fileLines):
		curLine = fileLines[LP]
		splitLine = curLine.split()
		
		if len(splitLine) == 4: #N, F, M, A
			peopleCount = int(splitLine[0])
			linkCount = int(splitLine[1])
			partyCount = int(splitLine[2])
			partyHostCount = int(splitLine[3])
			partyHostIDs = []
			LP += 1
			if DEBUG:
				print "Test case:",curTestCase + 1
				print " People:", peopleCount
				print " Friendships:", linkCount
				print " Parties:", partyCount
				print " Hosts:", partyHostCount

		for lineNum in range(LP, linkCount+LP):
			curLine = fileLines[LP]
			splitLine = curLine.split()
			socialGraph.add_edge(int(splitLine[0]),int(splitLine[1]))
			#print LP+1,"adding edge", splitLine[0],"and",splitLine[1]
			LP += 1	
		if partyHostCount != 0:
			for lineNum in range(LP,partyHostCount+LP):
				partyHostIDs.append(int(fileLines[lineNum]))
				LP += 1
			#print "partyHostIDs:",partyHostIDs
		
		curTestArray = [socialGraph,partyCount,partyHostIDs]
		parserOutput.append(curTestArray)
		curTestCase += 1

parseFileLines(socialGraphFile)	
#print "parser output:",parserOutput

#iterate over all the test cases now that they are processed into networkx graphs
for counter, test in enumerate(parserOutput):
	#test = [graph, partyCount, hosts]
	#					0					1					2
	curGraph = test[0]
	partyCount = test[1]
	hosts = test[2]
	people = nx.nodes(curGraph)
	peopleCount = len(people)
	print "Test Case",counter+1
	
	#part 1
	if len(hosts) == 1:
		awkwardValues = pc.calcAwkwardValues(curGraph,hosts[0])
		avg = pc.calcAvgAwk(awkwardValues,hosts)
		print "Average social awkwardness =", avg
	
	#part 2 
	elif len(hosts) > 1:
		awkVals = pc.bestAwkVals(curGraph,people,hosts)
		avg = pc.calcAvgAwk(awkVals,hosts)
		print "Average social awkwardness =", avg
		
	#part 3
	elif len(hosts) == 0:
		#Greedy Heuristic 1
		chosenHosts = pc.mostPopular(curGraph,people,partyCount)
		print "Heuristic 1 hosts are",chosenHosts
		avkVals = pc.bestAwkVals(curGraph, people, chosenHosts)
		avg = pc.calcAvgAwk(awkVals,chosenHosts)
		print "Average social awkwardness =", avg 
		
		#Greedy Heuristic 2
		chosenHosts = []
		availablePeople = list(people)
		mostPopular = pc.mostPopular(curGraph, people, 1)[0]
		chosenHosts.append(mostPopular)
		availablePeople.remove(mostPopular)
		for i in range(1,partyCount):
			awkVals = pc.bestAwkVals(curGraph, people, chosenHosts)
			curPartyHost = pc.mostAwkward(awkVals, availablePeople)
			chosenHosts.append(curPartyHost)
			availablePeople.remove(curPartyHost)
			
		print "Heuristic 2 hosts are",chosenHosts
		awkVals = pc.bestAwkVals(curGraph,people,chosenHosts)
		avg = pc.calcAvgAwk(awkVals,chosenHosts)
		print "Average social awkwardness =", avg

	#part 4

	
