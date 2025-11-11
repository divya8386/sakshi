 
v = int(input("Enter the number of vertices in the graph: ")) 
 
print("\n----------------------------------------------------\n") 
 
graph = [[0 for _ in range(v)]for _ in range(v)] 
 
for i in range(v): 
    for j in range(v): 
        weight = int(input(f"Enter the weight from {chr(i+65)} to {chr(j+65)}: ")) 
        graph[i][j] = weight 
 
print("\n----------------------------------------------------\n")   
 
def prims(graph, v): 
 
    selected = [0] * v 
    edges = 0 
    x = 0 
    y = 0 
    cost = 0 
 
    selected[0] = 1 
    while (edges < v-1): 
        mini=99 
        for i in range(v): 
            if(selected[i]): 
                for j in range(v): 
                    if (not selected[j] and graph[i][j]): 
                        if mini > graph[i][j]: 
                            mini = graph[i][j] 
                            x = i 
                            y = j 
        print(f"From {chr(65+x)} to {chr(65+y)} weight is {mini}.") 
        cost += mini 
        selected[y] = 1 
        edges += 1 
    
    print(f"The total cost of minimum spanning tree(traversal) is {cost}.") 
 
prims(graph, v) 