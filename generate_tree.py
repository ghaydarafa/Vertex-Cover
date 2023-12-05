import random

def save_graph_to_file(graph, filename):
    with open(filename, 'w') as f:
        f.write(f"{len(graph)}\n")
        for vertex, edges in graph.items():
            f.write(f"{' '.join(map(str, edges))}\n")

def generate_tree(size_dp, bnb_limit):
   graph = {i: [] for i in range(1, size_dp + 1)}

   # Connect each node to other nodes according to the tree
   for i in range(2, size_dp + 1):
       parent = random.randint(1, i - 1)
       graph[parent].append(i)
       graph[i].append(parent)

   # Create a sub-tree with the first bnb_limit vertices
   graph_bnb = {i: [] for i in range(1, bnb_limit + 1)}

   # For each vertex in the sub-tree, include all its edges that connect it with other vertices in the sub-tree
   for i in range(1, bnb_limit + 1):
       for j in graph[i]:
           if j in graph_bnb:
               graph_bnb[i].append(j)

   return graph, graph_bnb

dp = [10**4]
bnb = [60]
name = ['small']

for dp, bnb, name in zip(dp, bnb, name):
    graph_dp, graph_bnb = generate_tree(dp, bnb)
    save_graph_to_file(graph_dp, f"{name}_dp.graph")
    save_graph_to_file(graph_bnb, f"{name}_bnb.graph")