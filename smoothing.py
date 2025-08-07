# Smooth out degree 2 vertices
# Input: Graph G
# Output: G without degree 2 vertices

import networkx as nx
import matplotlib.pyplot as plt

def smoothing(G):
    G_smooth = G.copy()
    degree_2_vertices = [v for v in G_smooth if G_smooth.degree[v] == 2]
    
    for vertex in degree_2_vertices:
        n_1, n_2 = G_smooth.neighbors(vertex)
        G_smooth.remove_node(vertex)
        if not G_smooth.has_edge(n_1, n_2):
            G_smooth.add_edge(n_1, n_2)

    return G_smooth

# Testing
G = nx.Graph()
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(0,3)
G.add_edge(1,3)
G.add_edge(2,3)

H = smoothing(G)
print(H.edges())

# Create layout for the original graph
pos_G = nx.spring_layout(G, seed=42)        # Set seed for reproducibility

# Create first figure window for the original graph
plt.figure(1)
plt.title("Original Graph G")
nx.draw(G, with_labels=True, pos=pos_G, node_color='lightblue', node_size=500)

# Create second figure window for the subgraph using the same layout
plt.figure(2)
plt.title("Smoothed Graph")
# Use only the positions of nodes that exist in the subgraph
pos_H = {node: pos_G[node] for node in H.nodes()}
nx.draw(H, with_labels=True, pos=pos_H, node_color='lightcoral', node_size=500)

# Show both windows
plt.show()




