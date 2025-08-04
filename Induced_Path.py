# --- Induced Path --- #
# Input: Graph G, two vertices
# Output: induced path between two vertices

# Since the shortest path is always the induced path, shortest path is taken as the induced path

import networkx as nx
import matplotlib.pyplot as plt

def get_induced_path(G, v1, v2):
    induced_path = nx.shortest_path(G, v1, v2)
    return induced_path

# G=nx.Graph()
# G.add_edge(0,1)
# G.add_edge(1,2)
# G.add_edge(2,0)
# G.add_edge(2,3)
# G.add_edge(3,4)
# G.add_edge(4,5)
# G.add_edge(5,3)
# G.add_edge(4,2)

G = nx.petersen_graph()

induced_path = get_induced_path(G, 3, 5)
print(induced_path)

# Draw the original graph with highlighted induced path
plt.figure(1)
plt.title("Graph with Highlighted Induced Path")
pos_G = nx.spring_layout(G, seed=10)

# Create node colors - highlight path nodes in red, others in light green
node_colors = ['red' if node in induced_path else 'lightgreen' for node in G.nodes()]

# Create edge colors - highlight path edges in red, others in gray
path_edges = [(induced_path[i], induced_path[i+1]) for i in range(len(induced_path)-1)]
edge_colors = ['red' if edge in path_edges or (edge[1], edge[0]) in path_edges else 'gray' for edge in G.edges()]

# Draw the graph
nx.draw(G, pos=pos_G, with_labels=True, node_color=node_colors, edge_color=edge_colors, width=2)

# Add a legend
plt.figtext(0.02, 0.02, f"Induced path from {induced_path[0]} to {induced_path[-1]}: {' -> '.join(map(str, induced_path))}", fontsize=10)

plt.show()