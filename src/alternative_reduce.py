#!/usr/bin/env python3 
# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path', required=True)
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--plot_path', required=True)
args = parser.parse_args() 

# imports
import re
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
from collections import Counter,defaultdict 

# load each of the input paths
datewise_counts = defaultdict(lambda: defaultdict(int))
for path in args.input_paths:
    date_match = re.search(r'20-\d\d-\d\d', path)
    if date_match:
        date = date_match.group()
    else:
        continue
    
    with open(path) as f:
        data = json.load(f)
        for hashtag in data:
            if hashtag in "_all":
                continue
            for lang,count in data[hashtag].items():
                datewise_counts[date][hashtag] += count

# write the output path
    with open(args.output_path,'w') as f:
        json.dump(datewise_counts, f, indent=4)

args.hashtags = ['#' + hashtag.lstrip('#') for hashtag in args.hashtags]

# Visualization
def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%y-%m-%d')

fig, ax = plt.subplots()
for hashtag in args.hashtags:
    print(f"Processing hashtag: {hashtag}")
    dates = []
    values = []
    for date, hashtags in datewise_counts.items():
        if hashtag in hashtags:
            dates.append(parse_date(date))
            values.append(hashtags[hashtag])
    if dates and values:
        dates, values = zip(*sorted(zip(dates, values)))
        ax.plot(dates, values, label=hashtag)
    else:
        print(f"No data found for hashtag: {hashtag}")

# Formatting the plot
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.xlabel('Day of the Year')
plt.ylabel('Number of Tweets')
plt.title('Hashtag Usage Over Time')
plt.legend()
plt.tight_layout()

plt.savefig(args.plot_path, format='png')
plt.close()
