import sys
import os
import datetime

title = input("Enter the post title: ")
filename_title = input("Enter the filename, separate words by '-' : ")
tags = input("Enter the post tags, separated by spaces or nothing for no tags: ")
category = input("Enter the post categories, separated by spaces or nothing for no categories: ")

title_arr = title.split(' ')

filename = str(datetime.date.today()) + '-' + filename_title

with open(os.path.join('_posts', filename + '.markdown'), 'w') as f:
	f.write('---\ntitle:\t\t"' + title + '"\ndate:\t\t')
	f.write(str(datetime.date.today()) + '\ntags:\t\t' + tags + '\n')
	if category:
		f.write('category:\t' + category + '\n')
	f.write('comment:\theader sizes are 2000x750\nheader:\n\timage:\t\t')
	f.write(str(os.path.join('assets', 'images', filename, 'header.jpg')))
	f.write('\n\tteaser:\t\t')
	f.write(str(os.path.join('assets', 'images', filename, 'header.jpg')))
	f.write('\n\tcaption\t\t')
	f.write('"Photo credit: [**Unsplash**](https://unsplash.com)"\n---\n\n')
	f.write('Start writing here.\n')

os.makedirs(os.path.join('assets', 'images', filename)) # TODO: PROPER ERROR HANDLING