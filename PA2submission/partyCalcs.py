import networkx as nx
import operator
import random

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

#isIncidentWith
#determines if the given node is incident with any node in the given list.
def isIncidentWith(tarNode, nodes, edges):
	result = False
	if tarNode in nodes:
		result = True
	elif not len(nodes) == 0:
		for node in nodes:
			if (tarNode, node) in edges:
				result = True
			elif (node, tarNode) in edges:
				result = True
			else:
				result = False
	return result
 
#mostPopular
#takes in a graph, list of people, and desired result length
#returns a list of the most popular people 
def mostPopular(graph, people, num):
	if (num > people):
		print "failed! popular people > available people!"
	chosenPeople = []
	degrees = graph.degree(people)
	sortedDeg = sorted(degrees.items(), key=operator.itemgetter(1), reverse = True)
	for i in range(0, num):
		chosenPeople.append(sortedDeg[i][0])
	return chosenPeople

#mostPopularT4
#determines a list of the most popular people without the most popular people being incident to each other. 
def mostPopularT4(graph, people, partyCount):
	chosenPeople = []
	degrees = graph.degree(people)
	edges = graph.edges()
	mostPop = mostPopular(graph, people, len(people))

	for i in range(0, partyCount):
		j = 0 #init j
		#pick j from degrees, if j is incident with any in chosenPeople, pick j++
		chosenPerson = mostPop[j]
		while isIncidentWith(chosenPerson, chosenPeople, edges):
			j += 1
			chosenPerson = mostPop[j]
		chosenPeople.append(chosenPerson)
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

