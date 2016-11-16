import networkx as nx
import sys
import file2nx
 
f = open(sys.argv[1])
socialGraphFile = f.readline()
f.close()

parserOutput = file2nx.parseFileLines(socialGraphFile)

#parserOutput = "WHY IS THIS BREAAKING??!"
print parserOutput
