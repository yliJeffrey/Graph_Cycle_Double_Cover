# Original implementation adapted from Minjae Park
# 20106911 Minjae Park
# Finding an Ear decomposition of 2(-edge)-connected graph

import networkx as nx
import matplotlib.pyplot as plt

colorList = ["orange", "blue", "red", "green", "magenta", "purple", "yellow", "black"]
global count
count=0

'''
Input Graph
'''
# Complete Graph
# G=nx.complete_graph(4)


# # Non 2-connected (but 2-edge-connected) Graph
# G=nx.Graph()
# G.add_edge(0,1)
# G.add_edge(1,2)
# G.add_edge(2,0)
# G.add_edge(2,3)
# G.add_edge(3,4)
# G.add_edge(4,5)
# G.add_edge(5,3)
# G.add_edge(4,2)

# G = nx.Graph()
# G.add_edge(0,1)
# G.add_edge(0,2)
# G.add_edge(0,3)
# G.add_edge(1,2)
# G.add_edge(1,3)
# G.add_edge(2,3)


# Petersen Graph
G=nx.petersen_graph()

'''
Testing 2-edge-connectivity
'''
for e in list(G.edges()):
    H=nx.Graph(G)
    G.remove_edge(*e)
    if not nx.is_connected(G):
        raise SystemExit("G is not 2-edge-connected. This algorithm is not valid.")
    G=H

'''
Testing 2-connectivity
'''
for v in list(G.nodes()):
    H=nx.Graph(G)
    G.remove_node(v)
    if not nx.is_connected(G):
        print("G is not 2-connected. The result is not an open ear decomposition.")
    G=H

'''
Algorithm for Finding an Ear Decomposition
'''
def makeSpanningTree(G,root):
    T=nx.Graph()
    T.add_node(root)
    T.nodes[root]['dfsnum']=len(T.nodes())
    makeSpanningTreeDFS(G,T,root)
    return T

def makeSpanningTreeDFS(G,T,current):
    if not 'child' in T.nodes[current]:
        T.nodes[current]['child']=[]
    for neighbor in G.neighbors(current):
        if not neighbor in T.nodes():
            T.add_node(neighbor)
            T.add_edge(current,neighbor)
            T.nodes[neighbor]['dfsnum']=len(T.nodes())
            T.nodes[neighbor]['parent']=current
            T.nodes[current]['child'].append(neighbor)
            makeSpanningTreeDFS(G,T,neighbor)

def assignNonTreeEdgeLabel(G,T,current):
    global count
    subrootdfsnum=T.nodes[current]['dfsnum']
    for node,nodeattr in T.nodes(data=True):
        if nodeattr['dfsnum']>subrootdfsnum:
            if ((current,node) in G.edges() or (node,current) in G.edges()) and not ((current,node) in T.edges() or (node,current) in T.edges()):
                G[current][node]['label']=count
                count+=1
    for neighbor in T.nodes[current]['child']:
        assignNonTreeEdgeLabel(G,T,neighbor)

def assignTreeEdgeLabel(G,T,current):
    if not T.nodes[current]['child']:
        label=[]
        for neighbor in G.neighbors(current):
            if 'label' in G[current][neighbor]:
                label.append(G[current][neighbor]['label'])
        if 'parent' in T.nodes[current]:
            parent=T.nodes[current]['parent']
            G[current][parent]['label']=min(label)
    else:
        for neighbor in T.nodes[current]['child']:
            if not 'label' in T.nodes[neighbor]:
                assignTreeEdgeLabel(G,T,neighbor)
        if 'parent' in T.nodes[current]:
            parent=T.nodes[current]['parent']
            label=[]
            for neighbor in G.neighbors(current):
                if 'label' in G[current][neighbor]:
                    label.append(G[current][neighbor]['label'])
            G[current][parent]['label']=min(label)


def analyzeEar(ear_number, ear_list):
    """
    Analyze a specific ear and provide detailed information
    """
    if ear_number >= len(ear_list) or not ear_list[ear_number]:
        print(f"Ear {ear_number} is empty or doesn't exist")
        return
    
    ear_edges = ear_list[ear_number]
    print(f"\n=== DETAILED ANALYSIS OF EAR {ear_number} ===")
    print(f"Edges: {ear_edges}")
    
    # Find all vertices in this ear
    vertices = set()
    for edge in ear_edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    
    print(f"Vertices: {sorted(list(vertices))}")
    print(f"Number of edges: {len(ear_edges)}")
    print(f"Number of vertices: {len(vertices)}")
    
    # Determine ear type
    if len(ear_edges) == 1:
        print("Type: Single edge (simple ear)")
    elif len(ear_edges) == len(vertices):
        print("Type: Cycle (closed ear)")
    else:
        print("Type: Path or complex structure")
    
    # Check if it forms a path or cycle
    vertex_degree = {}
    for vertex in vertices:
        vertex_degree[vertex] = 0
    
    for edge in ear_edges:
        vertex_degree[edge[0]] += 1
        vertex_degree[edge[1]] += 1
    
    endpoints = [v for v, degree in vertex_degree.items() if degree == 1]
    internal_vertices = [v for v, degree in vertex_degree.items() if degree == 2]
    
    if endpoints:
        print(f"Endpoints (degree 1): {endpoints}")
    if internal_vertices:
        print(f"Internal vertices (degree 2): {internal_vertices}")
    
    return ear_edges

def get_ear_decomposition(G):
    T=makeSpanningTree(G,0)
    assignNonTreeEdgeLabel(G,T,0)
    assignTreeEdgeLabel(G,T,0)

    pos=nx.circular_layout(G)
    ear_list=[[] for i in range(count+1)]
    for (x,y) in G.edges():
        ear=G[x][y]['label']
        ear_list[ear].append((x,y))
    
    return ear_list


def main():

    # T=makeSpanningTree(G,0)
    # assignNonTreeEdgeLabel(G,T,0)
    # assignTreeEdgeLabel(G,T,0)

    # '''
    # Output
    # '''
    # pos=nx.circular_layout(G)
    # ear_list=[[] for i in range(count+1)]
    # for (x,y) in G.edges():
    #     ear=G[x][y]['label']
    #     ear_list[ear].append((x,y))

    ear_list = get_ear_decomposition(G)
    pos = nx.circular_layout(G)

    # Print detailed information about each ear
    print("=== EAR DECOMPOSITION RESULTS ===")
    print(f"Total number of ears found: {count}")
    print()

    for i in range(len(ear_list)):
        if ear_list[i]:  # Only print non-empty ears
            print(f"Ear {i}: {ear_list[i]}")
            print(f"  - Number of edges: {len(ear_list[i])}")
            print(f"  - Color: {colorList[i%len(colorList)]}")

            # Find unique vertices in this ear
            vertices_in_ear = set()
            for edge in ear_list[i]:
                vertices_in_ear.add(edge[0])
                vertices_in_ear.add(edge[1])
            print(f"  - Vertices involved: {sorted(list(vertices_in_ear))}")
            print()

    print("Raw ear_list:", ear_list)
    print()

    # Analyze each ear individually
    for i in range(len(ear_list)):
        if ear_list[i]:  # Only analyze non-empty ears
            analyzeEar(i, ear_list)

    print("\n" + "="*50)
    print("SUMMARY: How to find each ear")
    print("="*50)
    print("1. Ear 0 (orange): The initial structure - usually contains the spanning tree edges")
    print("2. Subsequent ears: Each adds connectivity by connecting previously separate parts")
    print("3. Each ear is a path where endpoints connect to already-constructed parts")
    print("4. Look for the pattern: ear endpoints attach to vertices from earlier ears")

    # Visualization
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_labels(G,pos)
    for i in range(len(ear_list)):
        if ear_list[i]:  # Only draw non-empty ears
            nx.draw_networkx_edges(G,pos,edgelist=ear_list[i],edge_color=colorList[i%len(colorList)],alpha=0.5,width=3)

    # Create edge labels showing ear numbers
    edge_labels = {}
    for (x,y) in G.edges():
        ear_num = G[x][y]['label']
        edge_labels[(x,y)] = f"E{ear_num}"

    nx.draw_networkx_edge_labels(G,pos,edge_labels,alpha=0.7)

    plt.title("Ear Decomposition - Each color represents a different ear")
    plt.show()

if __name__ == "__main__":
    main()