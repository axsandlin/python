#!/usr/bin/python

#This is my first python script to read the id3 tags from mp3 files and export them to a JSON file.

#Aubri Sandlin

#Feb. 02, 2014

#import eyed3

import os

dir = "/Volumes/music/unsorted"

music_list = os.listdir(dir)

f = open('/Users/axsandlin/workspaces/python/mp3_list','w')

for x in music_list:
   print x
   f.write(x) 

f.close()


# Assignment #1
# Look up how to get dir contents. I think this requires a module.
# use a for loop to print a list of files in this directory.

#for d in dircontents:
#   print d

# Assignment #2
# Use the system module to check if each is a file or a directory & display on the screen.


# Assignment #3
# use an if / else condition to append each directory to an array and display each file on the screen.


 
