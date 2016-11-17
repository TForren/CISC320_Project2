import networkx as nx

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

#bestAwkVals
#calculates the awkwardness of each person if they attend the party hosted by the host they know best. 
#takes in a graph and list of host ids
#returns the avg social awkwardness (int)
def bestAwkVals(graph, hosts):
	bestAwkVals = {}
	hostEval = {}
	avg = 0
	for host in hosts:
		curHostEval = calcAwkwardValues(graph, host)
		hostEval[host] = curHostEval
	for person in people:
		curBest = float('inf')
		for host in hostEval:
			curHostEval = hostEval[host]
			if curHostEval[person] < best:
				curBest = curHostEval[person]
		bestAwkVals[person] = curBest
	for person in bestAwkVals:
		if (bestAwkVals[person] != 0):
			avg = avg + bestAwkVals[person]
	avg = float(avg) / float(personCount - len(hosts))
	return avg


