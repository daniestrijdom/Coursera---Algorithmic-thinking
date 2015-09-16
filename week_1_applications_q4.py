'''
Module 1: Algorithmic Thinking: Application
@author: Danie Strijdom; Sep 2015
Question 3
'''

# general imports
import matplotlib.pyplot as plt
import random

class DPATrial:
    '''
    # provided to correctly create DPA graph
    '''
    
    def __init__(self, num_nodes):
        
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]
        print self._node_numbers

    def run_trial(self, num_nodes):
       
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def make_complete_graph(num_nodes):
    '''
    # function that takes a number of nodes as an input 
    # and return a completed graphs (all possible nodes connected)
    '''    
    completed_graph = {}    
    
    for i in range(num_nodes):
        completed_graph[i] = set(range(i)+range(i+1,num_nodes))
    
    return completed_graph

def compute_in_degrees(digraph):
    '''
    # function that take a directed graph and returns a new graph 
    # which shows the number of in-degress each node has
    '''

    in_degree_graph = {}                             
        
    # appends all in degree values to a list       
    for key in digraph.keys():
        in_degree_graph[key] = 0
        for val in digraph.values():
            if key in val:
                in_degree_graph[key] +=1            
    
    print 'DONE: compute_in_degrees'
    #print "In degree graph: ", in_degree_graph    
    return in_degree_graph

# compute_in_degrees(test_case)

def in_degree_distribution(digraph):
    '''
    # this function returns a graph that shows how many nodes have a specified
    # number of in_degrees
    '''
    
    # initialisations
    result = {}
    compute_graph = compute_in_degrees(digraph)          
    max_in_nodes = max(compute_graph.values())+1
    
    # creates the distribution
    for key in range(max_in_nodes):
        result[key] = 0
        for val in compute_graph.values():
            if key == val:
                result[key] += 1
                       
        if result[key] == 0:
            del result[key]
            
    # normalisation
            
    total = sum(compute_graph.values())
    print 'total: ',total
    
    for c in result:
        result[c] /= float(total)
    
        
    print 'DONE: in_degree_distribution'    
    return result

# ATTEMPT: DPA with n = 27,770, m = 13
# STEP 1: create completed graph with m = 5 nodes
n = 27770
m = 13

graph = make_complete_graph(m)

# STEP 2: create other 15 nodes, one at a time, 
testcase = DPATrial(m)

for new_node in range(n-m):
    graph[m+new_node] = testcase.run_trial(m)
    

data = in_degree_distribution(graph)




# plotting the data
plt.loglog(data.keys(),data.values(),'bo')
plt.xlabel('# In-nodes')
plt.ylabel('Distribution')
plt.title('Normalised in-degree distribution: DPA(27770,13)')
plt.show()
