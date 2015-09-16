''' 
Algoriothmic thinking : Project 1 
Author: Danie Strijdom 
September 2015

'''
import matplotlib.pyplot as plt

# example directed graphs
EX_GRAPH0 = {'A': set(['B','C','D']), 
             'B': set(['C','D']), 
             'C': set([]),
             'D': set([])}
             

EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
             
EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}

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
    for i in digraph.keys():
        in_degree_graph[i] = 0
        for j in digraph.values():
            if i in j:
                in_degree_graph[i] +=1            
    
    print 'DONE: compute_in_degrees'
    return in_degree_graph
 
def in_degree_distribution(digraph):
    '''
    # this function returns a graph that shows how many nodes have a specified
    # number of in_degrees
    '''
    
    distribution_graph = {}
    compute_graph = compute_in_degrees(digraph)          
    a = len((set(compute_graph.values())))+1
    
    for x in range(a):
        distribution_graph[x] = 0
        for y in compute_graph.values():
            if x == y:
                distribution_graph[x] += 1
            
            
        if distribution_graph[x] == 0:
            del distribution_graph[x]
            
    # normalisation
    total = float(sum(distribution_graph.values()))   
    
    for c in distribution_graph:
        distribution_graph[c] /= total
            
    print 'DONE: in_degree_distribution'    
    print 'Normalised: ', distribution_graph
    return distribution_graph


in_degree_distribution(EX_GRAPH0) 
data = in_degree_distribution(EX_GRAPH2)   


plt.loglog(data.keys(),data.values(),'bo')

plt.xlabel('In-degrees')
plt.ylabel('Distribution per in-degree')
plt.title('Normalised in-degree distribution')
plt.show()
