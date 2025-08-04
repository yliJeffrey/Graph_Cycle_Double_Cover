import networkx as nx
import matplotlib.pyplot as plt

def edge_induced_subgraph(G, L):
    H = nx.Graph()  # or G.__class__() if G might be a different type
    H.add_edges_from(L)
    return H

# # Define the whole graph G
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# G=nx.Graph()
# G.add_edge(0,1)
# G.add_edge(1,2)
# G.add_edge(2,0)
# G.add_edge(2,3)
# G.add_edge(3,4)
# G.add_edge(4,5)
# G.add_edge(5,3)
# G.add_edge(4,2)

G=nx.complete_graph(4)


# L is a subset of edges
L = [(1,2),(0,3)]

H = edge_induced_subgraph(G, L)

print("Nodes in subgraph:", H.nodes())
print("Edges in subgraph:", H.edges())


# Create layout for the original graph
pos_G = nx.spring_layout(G, seed=42)        # Set seed for reproducibility

# Create first figure window for the original graph
plt.figure(1)
plt.title("Original Graph G")
nx.draw(G, with_labels=True, pos=pos_G, node_color='lightblue', node_size=500)

# Create second figure window for the subgraph using the same layout
plt.figure(2)
plt.title("Subgraph H (Edge-induced)")
# Use only the positions of nodes that exist in the subgraph
pos_H = {node: pos_G[node] for node in H.nodes()}
nx.draw(H, with_labels=True, pos=pos_H, node_color='lightcoral', node_size=500)

# Show both windows
plt.show()
