import sys
import os
import datetime

title = input("Enter the post title: ")
filename_title = input("Enter the filename, separate words by '-' : ")
# TODO: Show categories and tags
tags = input("Enter the post tags, separated by spaces or nothing for no tags: ")
category = input("Enter the post category, or nothing for no categories: ")

title_arr = title.split(' ')

filename = str(datetime.date.today()) + '-' + filename_title

os.makedirs(os.path.join('assets', 'images', filename)) # TODO: PROPER ERROR HANDLING
#os.makedirs(os.path.join('_posts')) # TODO: PROPER ERROR HANDLING

with open(os.path.join('_posts', filename + '.markdown'), 'w') as f:
    f.write('---\ntitle:    "' + title + '"\ndate:     ')
    f.write(str(datetime.date.today()))
    if tags:
        f.write('\ntags:     ' + tags + '\n')
    if category:
        f.write('category:\t' + category + '\n')
    f.write('comment:  header sizes are 2000x750\nheader:\n  image:    ')
    f.write(str(os.path.join('assets', 'images', filename, 'header.jpg')))
    f.write('\n  teaser:   ')
    f.write(str(os.path.join('assets', 'images', filename, 'header.jpg')))
    f.write('\n  caption:  ')
    f.write('"Photo credit: [**Unsplash**](https://unsplash.com)"\n---\n\n')
    f.write('Start writing here.\n')

