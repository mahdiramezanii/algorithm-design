
def prim_algorithm(graph):
    
    root = list(graph.keys())[0]
    
    result = []
    
    
    small_tree = set([root])
    
    number_small_tree = 1
    
    
    number_of_roos = len(graph)
    

    while number_small_tree < number_of_roos:
        
        
        candidate_edges = []
        
        for vertex in small_tree:
            for k, v in graph[vertex].items():
                
                if k not in small_tree:
                    candidate_edges.append((vertex, k, v))
        
        min_edge = min(candidate_edges, key=lambda x: x[2])
        
        result.append(min_edge)
        
        small_tree.add(min_edge[1])
        
        number_small_tree += 1
    
    return result


graph = {
    'A': {'B': 2, 'D': 7, 'E': 6},
    'B': {'A': 2, 'C': 5},
    'C': {'B': 5, 'D': 1},
    'D': {'A': 7, 'C': 1, 'E': 4},
    'E': {'A': 6, 'D': 4}
}


    
def get_information():


    input_Gragh={}
    result={}

    flag=True

    while (flag):

        result.clear()
    
        top=input('Enter top: ')
        if top=="0":
            flag=False
            break
        n=int(input("Enter N: "))
    
        for i in range(n):
        
            widget=int(input("Enter Vazn: "))
            mane=input("Enter mane: ")
            result[widget]=mane

        test=result.copy()

        input_Gragh[top]=test

    return input_Gragh


#graph_2=get_information()
tree_edges = prim_algorithm(graph)

print(tree_edges)