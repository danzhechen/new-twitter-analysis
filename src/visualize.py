#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--graph_number', type=int, required=True)
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort the count values and select the top 10 keys
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

top_items = items[:10]
top_items_sorted = sorted(top_items, key=lambda item:(item[1],item[0]))


# Create a bar graph
plt.figure(figsize=(10, 6))
for key,value in top_items_sorted:
    plt.bar(key, value, color='skyblue')
plt.xlabel('Country Codes')
plt.ylabel('Tweet Counts')
plt.xticks(rotation='vertical')
plt.title('Top 10 Countries by Tweet Counts')
plt.tight_layout()

plt.savefig(f'reduced_bargraph_{args.graph_number}.png')
