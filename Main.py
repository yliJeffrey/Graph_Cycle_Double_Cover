# Find the Cycle Double-Cover Given a Bridgeless Subcubic Graph
# Input: bridgeless subcubic graph G
# Output: cycle double-cover

import networkx as nx
import matplotlib.pyplot as plt
from Ear_Decomposition import get_ear_decomposition
from Intersection_Graph import get_intersection_graph
from CDC_Cycles_Share_Vertex import get_vertex_sharing_cycles
from Subgraph_Construction import edge_induced_subgraph

'''
Step 1: Ear Decomposition
Induction Step {
    Step 2: Form Intersection Graph
    Step 3: Find Induced Path between two vertices
    Step 4: 
    Step 5:
    Step 6:
}
'''

# Check if an edge is shared by at least two cycles in the cycle list.
def is_shared_edge(cycle_list, edge):
    count = 0
    # Handle both orientations of the edge since the graph is undirected
    edge_reversed = (edge[1], edge[0])
    
    for cycle in cycle_list:
        if edge in cycle or edge_reversed in cycle:
            count += 1
            if count >= 2:
                return True
    
    return False

def get_cycle_double_cover(G):
    ear_list = get_ear_decomposition(G)


def induction_step(G, cycle_double_cover, u, w):
    intersection_graph = get_intersection_graph(G, cycle_double_cover)
    u_shared_cycles = get_vertex_sharing_cycles(cycle_double_cover, u)
    w_shared_cycles = get_vertex_sharing_cycles(cycle_double_cover, w)
    
    miminum_cycle_path = nx.shortest_path(intersection_graph, cycle_double_cover.index(u_shared_cycles[0]), cycle_double_cover.index(w_shared_cycles[0]))
    if miminum_cycle_path[1] == u_shared_cycles[1]:
        miminum_cycle_path.pop(0)
    if miminum_cycle_path[-2] == w_shared_cycles[1]:
        miminum_cycle_path.pop(-1)

    # Get all the edges in Minimum Cycle Path (MCP)
    mcp_edges = set()
    for cycle in miminum_cycle_path:
        mcp_edges.update(cycle_double_cover[cycle])
    print(f"mcp_edges: {mcp_edges}")

    # Subgraph Construction
    subgraph = edge_induced_subgraph(mcp_edges)
    subgraph.add_edge(u,w)
    plt.title("subgraph")
    nx.draw(subgraph, with_labels=True)
    plt.show()


    return intersection_graph, u_shared_cycles, w_shared_cycles, miminum_cycle_path

def main():
    G = nx.Graph()
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,3)
    G.add_edge(1,3)
    G.add_edge(2,3)
    
    pos_G = nx.spring_layout(G, seed=42)
    nx.draw(G, pos=pos_G, with_labels=True)
    plt.show()

    cycle_double_cover = [{(0,1),(1,3),(0,3)}, {(0,1),(1,3),(2,3),(0,2)}, {(0,3),(2,3),(0,2)}]
    H, U, W, mcp = induction_step(G, cycle_double_cover, 1, 2)
    nx.draw(H, with_labels=True)
    plt.show()

    for cycle in U:
        print(cycle)

    print()
    for cycle in W:
        print(cycle)

    print()
    print(mcp)


if __name__ == "__main__":
    main()