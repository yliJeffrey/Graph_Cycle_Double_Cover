import networkx as nx
import matplotlib.pyplot as plt

def two_edge_coloring(graph):
    color_map = {}  # key: edge (u, v), value: 0 or 1 (two colors)

    visited_edges = set()

    def dfs(u, prev_color):
        for v in graph.neighbors(u):
            edge = tuple(sorted((u, v)))
            if edge not in visited_edges:
                current_color = 1 - prev_color
                color_map[edge] = current_color
                visited_edges.add(edge)
                dfs(v, current_color)

    for node in graph.nodes:
        for neighbor in graph.neighbors(node):
            edge = tuple(sorted((node, neighbor)))
            if edge not in visited_edges:
                color_map[edge] = 0
                visited_edges.add(edge)
                dfs(neighbor, 0)

    return color_map

# You can switch between path_graph(n) or cycle_graph(n)
G = nx.cycle_graph(4)  # Try nx.path_graph(4) to test the path instead

# Apply edge coloring
coloring = two_edge_coloring(G)

# Draw the graph
pos = nx.spring_layout(G)  # Positions for nodes

# Separate edges by color
red_edges = [edge for edge, color in coloring.items() if color == 0]
blue_edges = [edge for edge, color in coloring.items() if color == 1]

plt.figure(figsize=(6, 4))
nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=600)
nx.draw_networkx_labels(G, pos, font_color='black')
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=2)
nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='blue', width=2, style='dashed')

plt.title("2-Edge Coloring of Graph")
plt.axis('off')
plt.show()
