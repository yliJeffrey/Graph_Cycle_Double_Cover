# --- Form intersection graph --- #
# Input: arbitrary number of lists of edges
# Output: an intersection graph

import networkx as nx
import matplotlib.pyplot as plt

def get_intersection_graph(G, edges_list):
    H = nx.Graph()
    for i in range(len(edges_list) - 1):
        for j in range(i + 1, len(edges_list)):
            if len(edges_list[i].intersection(edges_list[j])) != 0:     # draw an edge if two sets have non-empty intersection
                H.add_edge(i,j)
    return H

def main():
    G = nx.complete_graph(5)
    edges_list = [{(1,2),(2,3),(1,3)}, {(1,3),(1,4),(3,4)}, {(0,3),(0,4),(3,4)}]
    H = get_intersection_graph(G, edges_list=edges_list)

    print(f"The collection of edge sets: ")
    v = 0
    for edges in edges_list:
        print(f"{v}: {edges}")
        v += 1

    # Draw the original graph and intersection graph
    plt.figure(1)
    plt.title("Original Graph")
    pos_G = nx.spring_layout(G, seed=42)
    nx.draw(G, pos=pos_G, with_labels=True, node_color='lightgreen')

    plt.figure(2)
    plt.title("Intersection Graph")
    nx.draw(H, with_labels=True, node_color='lightgreen')
    plt.show()

if __name__ == "__main__":
    main()

