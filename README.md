# Twitter Hashtag Analysis v2

## Project Overview

This project involved analyzing Twitter data related to the BlackLivesMatter movement.
The goal was to track the usage and trends of various hashtags over time by scanning all geotagged tweets sent in 2020, providing insights into public discourse and sentiment surrounding the BlackLivesMatter movement.

## Methodology

The project was following the MapReduce procedure to analyze these tweets, which consists of three steps: partition, map, and reduce. The analysis was mainly conducted  in several phases:

1. **Data Procession (`map.py`)**:
   - Processed raw Twitter data based on the usage of the hashtags on both a language and country level.
   
2. **Data Aggregation (`reduce.py`)**:
   - Aggregated data across multiple files to create a comprehensive dataset.

3. **Data Visualization (`visualize.py` and `alternative_reduce.py`)**:
   - Developed scripts to visualize the aggregated data.
   - Generated bar graphs and line plots showing the frequency of specific hashtags over time and top 10 keys based on language and country.
   - Plots were created for each hashtag, providing a clear visual representation of trends and patterns.

## Results

Six PNG files were generated as a part of this analysis. First two plots represented how language and country was distributed by focusing on the usage of certain hashtags. The last two plots represented the comparison and contrast regarding the usage trends of different hashtags related to the BlackLivesMatter movement. These visualizations offer an intuitive understanding of how discussions evolved on Twitter over specific periods.

*Example Plots:*

### Use of the tag #blacklivesmatter in 2020 by language
![Plot 1](https://github.com/danzhechen/new-twitter-analysis/blob/main/plots/reduced_bargraph_1.png)

### Use of the tag #blacklivesmatter in 2020 by country
![Plot 2](https://github.com/danzhechen/new-twitter-analysis/blob/main/plots/reduced_bargraph_2.png)

### Use of the tag #blm in 2020 by Language
![Plot 3](https://github.com/danzhechen/new-twitter-analysis/blob/main/plots/reduced_bargraph_3.png) 

### Use of the tag #blm in 2020 by Language
![Plot 4](https://github.com/danzhechen/new-twitter-analysis/blob/main/plots/reduced_bargraph_4.png)
 
### Use of the tags #blacklivesmatter and #alllivesmatter in 2020
![Plot 5](https://github.com/danzhechen/new-twitter-analysis/blob/main/plots/hashtags_plot_1.png)

### Use of the tags #justice and #blm in 2020
![Plot 6](https://github.com/danzhechen/new-twitter-analysis/blob/main/plots/hashtags_plot_2.png)

