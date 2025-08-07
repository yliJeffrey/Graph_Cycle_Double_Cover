# --- CDC Cycles Share Vertex --- #
# Input: Cycle Double-Cover (CDC) & degree 2 vertex
# Output: 2 cycles in CDC using the degree 2 vertex

import networkx as nx
import matplotlib.pyplot as plt

def get_vertex_sharing_cycles(cycle_double_cover, v):
    vertex_sharing_cycles = []
    for cycle in cycle_double_cover:
        for edge in cycle:
            if v == edge[0] or v == edge[1]:
                vertex_sharing_cycles.append(cycle)
                break
    return vertex_sharing_cycles


def main():
    # Testing
    G = nx.Graph()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,3)
    G.add_edge(1,3)
    G.add_edge(2,3)

    cycle_double_cover = [[(0,2),(2,3),(3,0)], [(0,1),(1,3),(3,0)], [(0,1),(1,3),(3,2),(2,0)]]
    print(f"The Cycle Double-Cover:")
    for cycle in cycle_double_cover:
        print(cycle)
    print("\n")

    vertex_sharing_cycles = get_vertex_sharing_cycles(cycle_double_cover, 1)
    print("Vertex Sharing Cycles:")
    for cycle in vertex_sharing_cycles:
        print(cycle)

    pos_G = nx.spring_layout(G, seed=42)
    nx.draw(G, pos=pos_G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
