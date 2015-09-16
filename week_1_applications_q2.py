'''
Module 1: Algorithmic Thinking: Application
@author: Danie Strijdom; Sep 2015
'''
# general imports
import matplotlib.pyplot as plt
import random

def algorithm_ER(n,p):
    '''
    # Function for algorithm ER to create a directed graph
    '''    
    result = {}
    
    # make keys
    for key in range(n):
        result[key] = set([])
    
    # create directed edges 
    for key in result.keys():
        for val in range(n):
            test_p = random.uniform(0,1)
            if (test_p < p) and (key != val):
                result[key].add(val)
    
    print 'DONE: algorithm_ER'    
    print 'RESULT: ',result         
    return result
    
# test_case = algorithm_ER(5,0.5)    


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
    print "In degree graph: ", in_degree_graph    
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
    print 'In degree distribution:', result
    return result

# in_degree_distribution(test_case)


a = algorithm_ER(80,0.5)
data = in_degree_distribution(a)   

# plotting the data
plt.loglog(data.keys(),data.values(),'bo')
plt.xlabel('Nodes')
plt.ylabel('Distribution')
plt.title('Normalised in-degree distribution')
plt.show()