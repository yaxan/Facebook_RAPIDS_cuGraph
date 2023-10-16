import cugraph
import cudf
import networkx as nx
import matplotlib.pyplot as plt

# Assuming your file is a CSV containing source and destination of each edge
edge_list = cudf.read_csv('datasets/facebook_data.txt', delimiter=' ', names=['src', 'dst'], dtype=['int32', 'int32'])

# print(edge_list.head())  # Just to verify your data is loaded
G = cugraph.Graph()
G.from_cudf_edgelist(edge_list, source='src', destination='dst')

degrees = G.degrees()
#print("Degrees:\n", degrees)

# # Calculate PageRank scores
#pagerank_scores = cugraph.pagerank(G)
#print("Pagerank Scores:\n", pagerank_scores)

# You might want to use a subset of nodes for betweenness centrality because it's generally slow for larger networks
betweenness_centrality_scores = cugraph.betweenness_centrality(G)
print("Betweenness Centrality Scores: \n", betweenness_centrality_scores)

# # Compute the modularity optimization (Louvain) algorithm to find communities
# parts, modularity_score = cugraph.louvain(G)
# print(parts)
# print("Modularity was found to be {}".format(modularity_score))

# # Convert edge list from GPU to CPU
# edge_list_cpu = edge_list.to_pandas()

# # Create a new NetworkX graph from the edge list
# G_nx = nx.from_pandas_edgelist(edge_list_cpu, 'src', 'dst')

# # Draw the graph
# nx.draw(G_nx, with_labels=True)
# plt.show()
