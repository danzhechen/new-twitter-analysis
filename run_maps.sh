#!/bin/bash

# Directory where the tweet files are located
TWEET_DIR="/data/Twitter dataset"

# Loop through each file in the dataset (assuming the files are named in a way that includes the year)
for file in "$TWEET_DIR"/geoTwitter20-*.zip; do
    # Run map.py on each file
    python3 ./src/map.py --input_path="$file" &
done
