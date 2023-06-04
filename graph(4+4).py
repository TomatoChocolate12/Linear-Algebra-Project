import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create an instance of the bipartite graph
B = nx.Graph()

# Define the two sets of vertices
V1 = {'A', 'B', 'C'}
V2 = {'X', 'Y', 'Z'}

# Add the vertices to the graph
B.add_nodes_from(V1, bipartite=0)  # Set bipartite=0 for the first set
B.add_nodes_from(V2, bipartite=1)  # Set bipartite=1 for the second set

# Define the edges
edges = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]

# Add the edges to the graph
B.add_edges_from(edges)

# Add additional edges to connect the bipartite graph
extra_edges = [('A', 'Y'), ('B', 'Z')]
B.add_edges_from(extra_edges)

# Separate the vertices into two sets based on the bipartite attribute
X, Y = nx.bipartite.sets(B)

# Visualize the bipartite graph
pos = nx.bipartite_layout(B, X)

# Create a new figure for the first plot
plt.figure(1)

# Draw the vertices from each set with different colors
nx.draw_networkx_nodes(B, pos, nodelist=X, node_color='lightblue')
nx.draw_networkx_nodes(B, pos, nodelist=Y, node_color='lightgreen')

# Draw the edges
nx.draw_networkx_edges(B, pos)

# Draw labels for the vertices
nx.draw_networkx_labels(B, pos)

# Display the first plot
plt.axis('off')

adj_matrix = nx.to_numpy_matrix(B, nodelist=sorted(B.nodes()))

# Create a new figure for the second plot
plt.figure(2)

# Plot the adjacency matrix as a heatmap
plt.imshow(adj_matrix, cmap='viridis', interpolation='nearest')
plt.title('Adjacency Matrix')
plt.colorbar()

# Create a new figure for the third plot
plt.figure(3)

# Compute the eigenvalues
eigenvalues = np.linalg.eigvalsh(adj_matrix)

# Plot the eigenvalues in the 2-D complex plane
plt.scatter(np.real(eigenvalues), np.imag(eigenvalues), color='blue')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Eigenvalues in the Complex Plane')

# Set the plot background to black
plt.gca().set_facecolor('black')

# Add a centered grid
plt.grid(color='white', linestyle='dotted')

# Display the plots
plt.show()
