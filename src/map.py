#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--output_folder',default='outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load keywords
hashtags = [
    '#blacklivesmatter',
    '#blm',  
    '#alllivesmatter',    
    '#saytheirnames',
    '#justiceforgeorgefloyd',
    '#nojusticenopeace',
    '#icantbreathe',
    '#handsupdontshoot',
    '#stopasianhate',
    '#endracism',
    '#equity',
    '#defundthepolice',
    '#racism',
    '#civilrights',
    '#fightracism',
    '#justice',
    ]

# initialize counters
counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every file within the zip file
    for i,filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(),args.input_path,filename)

        # open the inner file
        with archive.open(filename) as f:

            # loop over each line in the inner file
            for line in f:

                # load the tweet as a python dictionary
                tweet = json.loads(line)

                # convert text to lower case
                text = tweet['text'].lower()

                lang = tweet['lang']

                country_info = tweet.get('place')
                if country_info and 'country_code' in country_info:
                    country_code = country_info['country_code']
                else:
                    country_code = 'Unknown'
                # search hashtags
                for hashtag in hashtags:
                    if hashtag in text:
                        counter_lang[hashtag][lang] += 1
                        counter_country[hashtag][country_code] += 1
                    counter_lang['_all'][lang] += 1
                    counter_country['_all'][country_code] += 1

# open the outputfile
try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))

output_path_lang = output_path_base+'.lang'
print('saving',output_path_lang)
with open(output_path_lang,'w') as f:
    f.write(json.dumps(counter_lang))

output_path_country = output_path_base+'.country'
print('saving',output_path_country)
with open(output_path_country,'w') as f:
    f.write(json.dumps(counter_country))
