import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt

def eigenvector_centrality(G, max_iter=100, tol=1.0e-6, nstart=None, weight='weight'):
    if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
        raise nx.NetworkXException("Not defined for multigraphs.")

    if len(G) == 0:
        raise nx.NetworkXException("Empty graph.")

    if nstart is None:
        # choose starting vector with entries of 1/len(G)
        x = dict([(n, 1.0/len(G)) for n in G])
    else:
        x = nstart

    # normalize starting vector
    s = 1.0 / sum(x.values())
    for k in x:
        x[k] *= s
    nnodes = G.number_of_nodes()

    # make up to max_iter iterations
    for i in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast, 0)

        # do the multiplication y^T = x^T A
        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)

        # normalize vector
        try:
            s = 1.0 / sqrt(sum(v**2 for v in x.values()))

        # this should never be zero?
        except ZeroDivisionError:
            s = 1.0
        for n in x:
            x[n] *= s

        # check convergence
        err = sum([abs(x[n]-xlast[n]) for n in x])
        if err < nnodes*tol:
            return x

    raise nx.NetworkXError("eigenvector_centrality(): power iteration failed to converge.")

# Create the graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])

# Plot the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray')

# Show the plot
plt.show()

# Compute eigenvector centrality
centrality = eigenvector_centrality(G)

# Print the centrality values
for node, centrality_value in centrality.items():
    print(f"Node {node}: {centrality_value}")
