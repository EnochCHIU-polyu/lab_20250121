import networkx as nx

def find_gatekeepers(graph):
    """
    Finds all gatekeeper nodes in the graph.
    A node X is considered a gatekeeper if for some nodes Y and Z, every path from Y to Z passes through X.
    """
    gatekeepers = set()
    nodes = list(graph.nodes)

    for x in nodes:
        for y in nodes:
            for z in nodes:
                if x != y and x != z and y != z:
                    # Temporarily remove node X
                    graph_removed = graph.copy()
                    graph_removed.remove_node(x)

                    # Check if Y and Z are disconnected in the modified graph
                    if not nx.has_path(graph_removed, y, z):
                        gatekeepers.add(x)
                        break  # No need to check further for this X
    return gatekeepers


def find_local_gatekeepers(graph):
    """
    Finds all local gatekeepers in the graph.
    A node X is considered a local gatekeeper if it has two neighbors Y and Z
    such that Y and Z are not directly connected.
    """
    local_gatekeepers = set()

    for x in graph.nodes:
        neighbors = list(graph.neighbors(x))
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                y, z = neighbors[i], neighbors[j]
                # Check if Y and Z are not directly connected
                if not graph.has_edge(y, z):
                    local_gatekeepers.add(x)
                    break  # No need to check further for this X
    return local_gatekeepers


# Example Graph
if __name__ == "__main__":
    # Create the graph and add edges as per your input
    G = nx.Graph()
    G.add_edge('D', 'B')
    G.add_edge('D', 'A')
    G.add_edge('D', 'C')
    G.add_edge('B', 'A')
    G.add_edge('C', 'A')
    G.add_edge('A', 'E')
    G.add_edge('A', 'F')
    G.add_edge('E', 'F')

    print("Graph edges:", G.edges)
    
    # Find gatekeepers
    gatekeepers = find_gatekeepers(G)
    print("Gatekeepers:", gatekeepers)

    # Find local gatekeepers
    local_gatekeepers = find_local_gatekeepers(G)
    print("Local Gatekeepers:", local_gatekeepers)