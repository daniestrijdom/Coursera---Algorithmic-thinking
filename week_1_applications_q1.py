'''
Module 1: Algorithmic Thinking: Application
@author: Danie Strijdom; Sep 2015
'''

import matplotlib.pyplot as plt

# import the dictionary from text file

data_set = {}
text_file = open('alg_phys-cite.txt')
for line in text_file:  
     a = line.strip().split()     
     data_set[a[0]] = (set(a[1:]))

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

 
data = in_degree_distribution(data_set)   

plt.loglog(data.keys(),data.values(),'bo')
plt.xlabel('# In-nodes')
plt.ylabel('Distribution')
plt.title('Normalised in-degree distribution: Citation Graph')
plt.show()