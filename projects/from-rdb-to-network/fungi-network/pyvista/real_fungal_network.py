import numpy as np
import pandas as pd

import networkx as nx

import pyvista
import streamlit as st

edges = pd.read_csv("./../data/sample-network.csv")
# Filters out very tiny weights for the purpose of a better visualisation
edges = edges[edges["weight"] >= 1]
# Changes to the correct format to easily add to networkx
edges = edges.to_dict("records")

G = nx.Graph()
for edge in edges:
    G.add_edge(edge["source"], edge["target"], weight=edge["weight"])

edge_weights = [G[u][v]["weight"] * 1.5 for u, v in G.edges]

pos = nx.spring_layout(G, seed=42, weight=None, dim=3)

coords = []
for value in pos.values():
    coords.append([value[0], value[1], value[2]])
coords = np.array(coords, dtype="float32")

print("Max coord:", coords.max())
print("Min Coord:", coords.min())

pdata = pyvista.PolyData(coords)
pdata['orig_sphere'] = np.arange(len(G.nodes))

# create many spheres from the point cloud
sphere = pyvista.Sphere(radius=0.02, phi_resolution=10, theta_resolution=10)
pc = pdata.glyph(scale=False, geom=sphere, orient=False)
pc.plot(cmap='Reds')
