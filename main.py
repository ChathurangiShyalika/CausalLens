from DiffAN import diffAN

# Create an instance
n_nodes = 10
diffan = diffAN(n_nodes, residue=False)

# Run causal discovery
diffan.fit()
