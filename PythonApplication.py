import os
import requests
import pandas as pd

url = 'https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz'
fname = os.path.basename(url)

if not os.path.isfile(fname):
    print(f"Downloading...\n{url}")
    r = requests.get(url, allow_redirects=True)
    open(fname, 'wb').write(r.content)
else:
    print(f"Already downloaded:\n{url}")
    
# parse the file
cols = ['source', 'target', 'rating', 'time']
df = pd.read_csv(fname, names=cols, header=None)
df['time'] = pd.to_datetime(df.time * 1e9)
df = df.set_index('time')

df.shape

df_ = df.loc['2014-03']
print("Ratings: {len(df_)}")
df_.sample(10)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import math

DG = nx.MultiDiGraph()
edges = [(t.source, t.target, float(t.rating)) for t in  df_.itertuples()]
DG.add_weighted_edges_from(edges)

print(f"Nodes: {DG.number_of_nodes()}")
print(f"Edges: {DG.number_of_edges()}")

# build a lookup of review counts and average trust rating
#review_counts = df_.groupby('target').rating.count()
#print(review_counts)
#average_reviews = df_.groupby('target').rating.mean()
#print(average_reviews)


#def get_size(user_id, m=200, min=300):
#    s = review_counts.get(user_id)
#    if s is not None:
#        return min * s
#    else:
#        return min

#def get_color(user_id):
#    s = average_reviews.get(user_id)
#    if s is None:
#        return 0.5
#    # need a scaling function to translate -10-10 to 0.0-1.0 for colors maps
#    return np.interp(s, (-10, 10), (0, 1))

#plt.figure(figsize=(14, 14)) 
#plt.title("Bitcoin Trust Network", fontsize=18)

#untrusted = mpatches.Patch(color='red', label='Negative Reputation')
#trusted = mpatches.Patch(color='green', label='Positive Reputation')
#size = mpatches.Patch(color='white', label='Node Size - Rating')
#edges = mpatches.Patch(color='white', label='Edge Length - Indicator of Trust Inversely')
#plt.legend(handles=[trusted, untrusted, size], loc='lower right')

#pos = nx.spring_layout(DG, k=0.25)
#sizes = [get_size(n) for n in DG]
#colors = [get_color(n) for n in DG]

#nc = nx.draw_networkx_nodes(DG, pos, nodelist=DG.nodes(), node_size=sizes, linewidths=2.0, node_color=colors, cmap=plt.cm.RdYlGn, alpha=0.8)

#ec = nx.draw_networkx_edges(DG, pos, arrows=True, alpha=0.08)
#ax = plt.axis('off')
#plt.show()

import cpalgorithm as cp

km = cp.KM_config();
km.detect(DG)
c = km.get_pair_id()
x = km.get_coreness()

#for k, v in sorted(c.items()):
#    print(k, v)

print("END! END! END! END! ")
sig_pair_id, sig_coreness, significance, p_values = cp.qstest(c, x, DG, km)

#x_sorted = {k: v for k, v in sorted(x.items(), key=lambda y: y[1])}

#for k, v in x_sorted.items():
#    print(k, v)

print('Name\tPairID\tCoreness')
for key, value in sorted(c.items(), key=lambda x: x[1]):
    print('%s\t%d\t%f' %(key, c[key], x[key]))

print("END! END! END! END! ")


#for id in x:
#    print (id, x[id])

#plt.figure(3,figsize=(8,6))
cmap = plt.cm.get_cmap('Set1')
pos = nx.spring_layout(DG, k=0.25)
node_colors = [cmap(c[d]) if x[d] ==1 else "white" for d in DG.nodes()]
node_edge_colors = [cmap(c[d]) if x[d] ==0 else "black" for d in DG.nodes()]
node_labels = [d for d in DG.nodes()]

nodes = nx.draw_networkx_nodes(DG, pos,  node_color = node_colors, linewidths=2)
nodes.set_edgecolor(node_edge_colors)
nx.draw_networkx_edges(DG, pos)
nx.draw_networkx_labels(DG, pos)

plt.gca().axis('off')
plt.show()