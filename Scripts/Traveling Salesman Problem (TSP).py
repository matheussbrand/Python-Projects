import random  # Importing the random module to generate random numbers.
import networkx as nx  # Importing NetworkX library for graph-related operations.
import matplotlib.pyplot as plt  # Importing Matplotlib library for plotting graphs.
from networkx.algorithms.approximation import traveling_salesman_problem  # Importing the traveling_salesman_problem function from NetworkX.

def generate_complete_graph(num_nodes, weight_range=(1, 100)):
    """
    Generate a complete graph with a specified number of nodes and assign random weights to its edges within a range.
    
    Parameters:
    - num_nodes: Number of nodes in the complete graph.
    - weight_range: Tuple representing the range for assigning random weights to edges (default: (1, 100)).
    
    Returns:
    - G: Complete graph with assigned edge weights.
    """
    G = nx.complete_graph(num_nodes)
    for u, v in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)
    return G

def plot_graph_step(G, tour, current_node, pos):
    """
    Plot the graph at each step of the algorithm with specific node and edge colors, and labels.
    
    Parameters:
    - G: Graph to be plotted.
    - tour: List representing the sequence of nodes visited.
    - current_node: Current node being visited.
    - pos: Positional layout of the nodes in the graph.
    """
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    path_edges = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='yellow', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='green', node_size=500)
    
    edges_labels = nx.get_edge_attributes(G, name='weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edges_labels)
    
    plt.pause(0.5)

def calculate_tour_cost(G, tour):
    """
    Calculate the total cost of the tour based on the weights of the edges traversed.
    
    Parameters:
    - G: Graph containing edge weights.
    - tour: List representing the sequence of nodes visited.
    
    Returns:
    - total_cost: Total cost of the tour based on edge weights.
    """
    total_cost = 0
    for i in range(len(tour) - 1):
        if G.has_edge(tour[i], tour[i + 1]):
            total_cost += G[tour[i]][tour[i + 1]]['weight']
        else:
            raise ValueError(f"Edge {tour[i]}-{tour[i + 1]} does not exist in the graph.")
    return total_cost

def nearest_neighbor_tsp(G, start_node=None):
    """
    Implement the nearest neighbor algorithm to solve the Traveling Salesman Problem (TSP).
    
    Parameters:
    - G: Graph representing the cities and distances between them.
    - start_node: Starting node for the algorithm (default: randomly chosen from nodes in the graph).
    """
    if start_node is None:
        start_node = random.choice(list(G.nodes))
        
    pos = nx.spring_layout(G)
    plt.ion()  # Turn on interactive mode for plotting.
    plt.show()
    
    unvisited = set(G.nodes)
    unvisited.remove(start_node)
    tour = [start_node]
    current_node = start_node
    
    plot_graph_step(G, tour, current_node, pos)
    
    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        unvisited.remove(next_node)
        current_node = next_node
        tour.append(current_node)
        plot_graph_step(G, tour, current_node, pos)
    
    tour.append(start_node)
    plot_graph_step(G, tour, current_node, pos)
    
    tour_cost = calculate_tour_cost(G, tour)
    print(f'Construction Heuristic Tour Cost: {tour_cost}')
    
    plt.ioff()  # Turn off interactive mode to display final result.
    plt.show()

if __name__ == '__main__':
    G = generate_complete_graph(5)  # Generating a complete graph with 5 nodes.
    
    approx_tour = traveling_salesman_problem(G, cycle=True)  # Finding an approximate TSP tour using a built-in function.
    approx_tour_cost = calculate_tour_cost(G, approx_tour)  # Calculating the cost of the approximate tour.
    
    print(approx_tour)  # Printing the approximate tour sequence.
    print(approx_tour_cost)  # Printing the cost of the approximate tour.
    
    nearest_neighbor_tsp(G)  # Applying the nearest neighbor algorithm to solve the TSP for the generated graph.
