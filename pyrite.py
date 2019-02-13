#!/usr/bin/env python3

import os
import datetime
import string

TITLE = input("Enter the post title: ").strip
FILENAME_TITLE = input("Enter the post filename: ")
# TODO: Show categories and tags
TAGS = input("Enter the post tags, separated by spaces or nothing for no tags: ")
CATEGORY = input("Enter the post category, or nothing for no categories: ")

FILENAME = str(datetime.date.today()) + '-' + FILENAME_TITLE + ".md"

os.makedirs(os.path.join('assets', 'images', FILENAME)) # TODO: PROPER ERROR HANDLING
#os.makedirs(os.path.join('_posts')) # TODO: PROPER ERROR HANDLING

with open(os.path.join('_posts', FILENAME + '.markdown'), 'w') as f:
    f.write('---\ntitle:    "' + TITLE + '"\ndate:     ')
    f.write(str(datetime.date.today()))
    if TAGS:
        f.write('\ntags:     ' + TAGS + '\n')
    if CATEGORY:
        f.write('category:\t' + CATEGORY + '\n')
    f.write('comment:  header sizes are 2000x750\nheader:\n  image:    ')
    f.write(str(os.path.join('assets', 'images', FILENAME, 'header.jpg')))
    f.write('\n  teaser:   ')
    f.write(str(os.path.join('assets', 'images', FILENAME, 'header.jpg')))
    f.write('\n  caption:  ')
    f.write('"Photo credit: [**Unsplash**](https://unsplash.com)"\n---\n\n')
    f.write('Start writing here.\n')
