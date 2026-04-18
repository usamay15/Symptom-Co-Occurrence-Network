# Symptom Co-Occurrence Network Dataset

This repository contains a structured JSON file representing a **symptom co-occurrence network** extracted from clinical observations. The dataset is intended for research and educational purposes in the fields of **social network analysis**, **network medicine**, and **health informatics**.

## Dataset Description

- **File**: `symptom_network.json`
- **Format**: JSON
- **Type**: Undirected weighted graph
- **Nodes**: Each node represents a unique symptom.
- **Edges**: Each edge indicates that the two symptoms co-occurred in at least one patient case.

### Upgraded Version

The current version of the dataset includes:

 **Edge Weights**: Indicating the number of co-occurrences between each symptom pair.
 **Node Notes**: Additional metadata fields now contain brief associations to diseases or conditions, where available.

## Usage

You can load and analyze the network using Python's [NetworkX](https://networkx.org/) library:

```python
import networkx as nx
import json

# Load the JSON file
with open('symptom_network.json') as f:
    data = json.load(f)

# Build the graph
G = nx.node_link_graph(data)

# Example: print basic info
print(nx.info(G))
```

## Calculator

This repository also includes a simple calculator script:

```bash
python calculator.py add 10 5
python calculator.py sub 10 5
python calculator.py mul 10 5
python calculator.py div 10 5
```
