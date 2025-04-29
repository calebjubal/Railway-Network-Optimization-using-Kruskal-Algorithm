import streamlit as st
import networkx as nx
import pandas as pd
from pyvis.network import Network

# Union-Find Data Structure (Disjoint Set)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

# Kruskal's Algorithm
def kruskal(n, edges):
    uf = UnionFind(n)
    mst = []
    edges = sorted(edges, key=lambda x: x[2])
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
    return mst

# Create pyvis graph
def create_interactive_graph(G):
    net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black")
    for node in G.nodes():
        net.add_node(node, label=str(node + 1), shape="circle", size=30, font=dict(size=20))
    for u, v, d in G.edges(data=True):
        net.add_edge(u, v, label=f"Cost: {d['weight']}")
    net.write_html("railway_network.html")

# Streamlit UI
st.title("Railway Network Optimization using Kruskal's Algorithm")

# Default mode toggle
use_default = st.checkbox("Use Default Graph (6 Cities with predefined edges)", value=True)

if use_default:
    num_cities = 6
    default_edges = [
        (0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10),
        (2, 3, 3), (2, 4, 8), (3, 4, 7), (3, 5, 6), (4, 5, 9)
    ]
    st.markdown("### Default Complex Graph Loaded")
    G = nx.Graph()
    edges = []
    for u, v, cost in default_edges:
        G.add_edge(u, v, weight=cost)
        edges.append((u, v, cost))
else:
    num_cities = st.number_input("Enter the number of cities:", min_value=2, max_value=20, value=5)
    G = nx.Graph()
    edges = []

    st.write("Add connections (edges) between cities:")
    for i in range(num_cities):
        st.write(f"Connections from City {i+1}:")
        num_connections = st.number_input(f"Number of connections from City {i+1}:", min_value=0, value=2, key=f"num_conn_{i}")
        for j in range(num_connections):
            city_to = st.number_input(f"City {i+1} to City (number):", min_value=1, max_value=num_cities, value=1, key=f"city_to_{i}_{j}")
            cost = st.number_input(f"Cost of connection to City {city_to}:", min_value=1, value=10, key=f"cost_{i}_{j}")
            if city_to != i+1:
                G.add_edge(i, city_to - 1, weight=cost)
                edges.append((i, city_to - 1, cost))

# Show network and MST
if st.button("Show Railway Network"):
    if len(edges) == 0:
        st.warning("No connections defined.")
    else:
        create_interactive_graph(G)
        st.markdown("### Interactive Railway Network Graph")
        with open("railway_network.html", "r") as f:
            st.components.v1.html(f.read(), height=600)

        mst = kruskal(num_cities, edges)
        total_cost = sum(w for _, _, w in mst)

        st.subheader("Optimal Railway Network (MST):")
        mst_df = pd.DataFrame(mst, columns=["City 1", "City 2", "Cost"])
        mst_df["City 1"] += 1
        mst_df["City 2"] += 1
        st.dataframe(mst_df, use_container_width=True)

        st.subheader(f"Total Cost of Railway Network: {total_cost}")
