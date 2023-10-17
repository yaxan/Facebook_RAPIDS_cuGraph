# RAPIDS cuGraph Analysis on Facebook Dataset

This project demonstrates the application of GPU-accelerated graph analytics through RAPIDS [cuGraph](https://github.com/rapidsai/cugraph) on a Facebook dataset provided by the [Stanford Network Analysis Project (SNAP)](https://snap.stanford.edu/data/ego-Facebook.html). By leveraging cuGraph functionalities, we perform various graph analytics methodologies including calculating degrees, PageRank, Betweenness Centrality, and community detection using the Louvain method.

## Background

The dataset represents a social network from Facebook. It consists of 'circles' (or 'friends lists') from Facebook. Facebook data was collected from survey participants using a Facebook app. The dataset includes node features (profiles), circles, and ego networks.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- NVIDIA GPU
- CUDA and cuDNN installed and configured
- [RAPIDS](https://docs.rapids.ai/install) suite installed (cuDF and cuGraph libraries)
- Python 3.x
- NetworkX and Matplotlib Python libraries installed
- The Facebook dataset from SNAP

### Script Operations

The script performs the following operations:

1. **Data Loading:** Loads the Facebook dataset and initializes a cuGraph graph.
2. **Degree Calculation:** Calculates the degree of each node in the network.
3. **PageRank Calculation:** Computes the PageRank scores for each node, highlighting influential users in the social network.
4. **Betweenness Centrality Calculation:** Computes the betweenness centrality scores for each node, identifying bridges or connectors in the social network.
5. **Community Detection:** Applies the Louvain method for community detection, categorizing users into distinct communities, and calculates the modularity score.
6. **Visualization:** Renders the network graph, color-coded based on community structure, using NetworkX and Matplotlib. It showcases the communities and highlights the relationships between users.

![Visualization of Network Graph](https://github.com/yaxan/Facebook_RAPIDS_cuGraph/assets/41130598/345c9541-e713-44d6-8005-fb78bbbfdd0f)
![Visualization of Network Graph with page rank](https://github.com/yaxan/Facebook_RAPIDS_cuGraph/assets/41130598/38f2b53e-d353-41a8-b4b8-6daf1f5fcd45)
![Visualization of Network Graph with Betweenness](https://github.com/yaxan/Facebook_RAPIDS_cuGraph/assets/41130598/aed929a3-3c67-4aab-92bd-23f3c6dea1f7)

