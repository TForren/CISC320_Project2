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

#avgAwkwardness
#takes in socialGraphnx, peopleCount, and party host ID
#returns the average social awkwardness if everyone attended the party (int)
def avgAwkwardness(socialGraph, peopleCount, hostID): 
	people = nodes(socialGraph)
	avg = 0
	#for person in people:
		#avg = avg +  

#takes in a list of people and the host IDs
#returns a floating point avg awkwardness across all 
#def calcAvgAwk(people, hostIDs):
