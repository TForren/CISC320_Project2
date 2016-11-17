import networkx as nx
import operator

#given n people and 1 party host, calculate average social awkardness if all people attended 

awkwardValues = []

#calcAwkwardValues
#takes in a social graph and a hostID
#returns a dictionary of awkward values for each person in the graph
def calcAwkwardValues(socialGraph, hostID):
	people = nx.nodes(socialGraph)
	awkwardValues = {}
	for person in people:
		awk = nx.shortest_path_length(socialGraph,hostID,person)
		awkwardValues[person] = awk
	return awkwardValues 

#calcAvg
#takes in a dictionary of awkward values and hosts
#returns the average social awkwardness omitting hosts
def calcAvgAwk(awkVals,hosts):
	avg = 0
	for person in awkVals:
		if (awkVals[person] != 0):
			avg = avg + awkVals[person]
	avg = float(avg) / float(len(awkVals) - len(hosts))
	return round(avg,2)

#bestAwkVals
#calculates the awkwardness of each person if they attend the party hosted by the host they know best. 
#takes in a graph, list of people, list of host ids
#returns the best awk vals dictionary
def bestAwkVals(graph, people, hosts):
	bestAwkVals = {}
	hostEval = {}
	personCount = len(people)
	avg = 0
	for host in hosts:
		curHostEval = calcAwkwardValues(graph, host)
		hostEval[host] = curHostEval
	for person in people:
		curBest = float('inf')
		for host in hostEval:
			curHostEval = hostEval[host]
			if curHostEval[person] < curBest:
				curBest = curHostEval[person]
		bestAwkVals[person] = curBest
	return bestAwkVals

#mostPopular
#takes in a graph, list of people, and desired result length
#returns a list of the most popular people 
def mostPopular(graph, people, num):
	if (num > people):
		print "Trying to find more popular people than people!"
	chosenPeople = []
	degrees = graph.degree(people)
	sortedDeg = sorted(degrees.items(), key=operator.itemgetter(1), reverse = True)
	for i in range(0, num):
		chosenPeople.append(sortedDeg[i][0])
	return chosenPeople

#mostAwkward
#takes in awkward values and a list of available people
#returns the most awkward sap out of them all
def mostAwkward(awkVals, availablePeople):
	curBest = (0,0) #(person,awkwardness) 
	for person in availablePeople:
			curAwk = awkVals[person]
			if curAwk > curBest[1]:
				curBest = (person,curAwk)
			elif curAwk == curBest[1]:
				if person < curBest[0]:
					curBest = (person,curAwk)
	return curBest[0]


