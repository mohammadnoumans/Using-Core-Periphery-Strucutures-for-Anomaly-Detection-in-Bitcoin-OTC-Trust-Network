#import os
#import requests
#import pandas as pd

#url = 'https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz'
#fname = os.path.basename(url)

#if not os.path.isfile(fname):
#    print(f"Downloading...\n{url}")
#    r = requests.get(url, allow_redirects=True)
#    open(fname, 'wb').write(r.content)
#else:
#    print(f"Already downloaded:\n{url}")
    
## parse the file
#cols = ['source', 'target', 'rating', 'time']
#df = pd.read_csv(fname, names=cols, header=None)
#df['time'] = pd.to_datetime(df.time * 1e9)
#df = df.set_index('time')

#df.shape

#df_ = df.loc['2014-03']
#print("Ratings: {len(df_)}")
#df_.sample(10)

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
#import networkx as nx
#import math

#DG = nx.MultiDiGraph()
#edges = [(t.source, t.target, float(t.rating)) for t in  df_.itertuples()]
#DG.add_weighted_edges_from(edges)

#print(f"Nodes: {DG.number_of_nodes()}")
#print(f"Edges: {DG.number_of_edges()}")

# #build a lookup of review counts and average trust rating
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
