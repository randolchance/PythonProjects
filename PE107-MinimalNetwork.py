"""
PROJECT EULER PROBLEM 107 - Minimal Network

The following undirected network consists of seven vertices and twelve
edges with a total weight of 243.

(NOT DISPLAYED)

The same network can be represented by the matrix below.

    	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-
However, it is possible to optimise the network by removing some edges
and still ensure that all points on the network remain connected.
The network which achieves the maximum saving is shown below. It has
a weight of 93, representing a saving of 243 − 93 = 150 from the
original network.


Using network.txt (right click and 'Save Link/Target As...'), a
6K text file containing a network with forty vertices, and given
in matrix form, find the maximum saving which can be achieved by
removing redundant edges whilst ensuring that the network remains
connected.
"""


from operator import itemgetter

def readNetwork():
    raw_network_list = []
    with open("p107_network.txt") as file:
        for line in file:
            row = line.rstrip("\n")
            row = row.split(",")
            raw_network_list.append(row)
    return(raw_network_list)

class Node:
    def __init__(self,ID):
        self.node_dict = {}
        self.ID = ID
    def __str__(self):
        return('NODE ' + str(self.ID))
    def setLink(self,node,weight):
        self.node_dict[node] = weight
    def delLink(self,node):
        self.node_dict.pop(node,None)
    def getLinks(self,*nodes):
        if nodes == []:
            return self.node_dict
        node_dict = {}
        for node in nodes:
            node_dict[node] = self.node_dict[node] if node in self.node_dict else '-'
        return(node_dict)
    def getNodes(self):
        return(list(self.node_dict.keys()))
    def getWeights(self,*nodes):
        if len(nodes) == 0:
            return(list(self.node_dict.values()))
        weight_list = []
        for node in nodes:
            weight_list.append(self.node_dict[node])
        return(weight_list)

def checkConnectivity(start_node,end_node,node_list):
    new_node_list = node_list + [start_node]
    for node in start_node.getNodes():
        if node == end_node:
            return True
        if node in new_node_list:
            continue
        if checkConnectivity(node,end_node,new_node_list):
            return True
    return False

def checkTotalConnectivity(start_node,node_list):
    if len(node_list) == 0:
        return True
    if start_node in node_list:
        node_list.remove(start_node)
        for node in start_node.getNodes():
            if checkTotalConnectivity(node,node_list):
                return True
        return False
    
                
def computeTotalWeight(weight_list):
    total_weight = 0
    for w in weight_list:
        total_weight += w[0]
    return(total_weight)
            

# Get raw network data
network_list = readNetwork()

# Build a list of nodes and add their link weights
nodes = []
for i,node_links in enumerate(network_list):
    node = Node(i)
    nodes.append(node)

# Generate and sort by weight a list of links
weight_list = []
for i,node_links in enumerate(network_list):
    for j,weight in enumerate(node_links):
        if weight != '-':
            nodes[i].setLink(nodes[j],int(weight))
            if j > i:
                weight_list.append([int(weight),nodes[i],nodes[j]])
weight_list.sort(key=itemgetter(0))
weight_list.reverse()

initial_total_weight = computeTotalWeight(weight_list)

WEIGHT = 0
NODE_A = 1
NODE_B = 2
for i,link in enumerate(weight_list[:]):
    print(i)
    node_a = link[NODE_A]
    node_b = link[NODE_B]
    weight = link[WEIGHT]
    
    node_a.delLink(node_b)
    node_b.delLink(node_a)
    if not checkConnectivity(node_a,node_b,[]):
        node_a.setLink(node_b,weight)
        node_b.setLink(node_a,weight)
    else:
        weight_list.remove(link)
        print(computeTotalWeight(weight_list))

final_total_weight = computeTotalWeight(weight_list)

diff_total_weight = initial_total_weight - final_total_weight
print("Initial network weight: " + str(initial_total_weight))
print("Final network weight: " + str(final_total_weight))
print("Difference: " + str(diff_total_weight))

print("Network is still connected: " + str(checkTotalConnectivity(nodes[0],nodes)))
