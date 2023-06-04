import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# Create an adjacency matrix for a sample graph
adjacency_matrix = np.array([[0, 1, 0],
                             [1, 0, 0],
                             [0, 0, 0],])

# Create a graph from the adjacency matrix
graph = nx.from_numpy_array(adjacency_matrix)

# Draw the graph
pos = nx.spring_layout(graph)  # Position the nodes using a spring layout algorithm
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold', edge_color='gray')

# Show the plot
plt.show()
# Compute the degree matrix
degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))

# Compute the Laplacian matrix
laplacian_matrix = degree_matrix - adjacency_matrix

# Calculate the eigenvalues of the Laplacian matrix
eigenvalues = np.linalg.eigvals(laplacian_matrix)

# Sort the eigenvalues in ascending order
sorted_eigenvalues = np.sort(eigenvalues)
sorted_eigenvalues[0]=0
# Find the second smallest eigenvalue
second_smallest_eigenvalue = sorted_eigenvalues[1]

# Check if the second smallest eigenvalue is approximately 0
if np.isclose(second_smallest_eigenvalue, 0):
    print("The graph is disconnected.")
else:
    print("The graph is connected.")
print("Laplacian Eigenvalues:")
print(sorted_eigenvalues)
indices = np.arange(len(eigenvalues))
plt.hlines(0, min(indices), max(indices), color='black', linewidth=1)
plt.plot(indices, np.zeros_like(indices), 'bo', markersize=5)

# Set the y-axis limits
plt.ylim(-1, 1)

# Plot the eigenvalues as tick marks
plt.vlines(indices, -0.05, 0.05, colors='red')

# Set the x-axis tick labels
plt.xticks(indices, eigenvalues)

plt.xlabel('Eigenvalue')
plt.title('Eigenvalue Spectrum of 1D Graph')
plt.show()