#!/usr/bin/python

#This is my first python script to read the id3 tags from mp3 files and export them to a JSON file.

#Aubri Sandlin

#Feb. 02, 2014

#import eyed3

#This import is to work with files and directories.

import os

music_dir = "/Volumes/music/unsorted"

#method for determining if object in path passed in is a file or directory.

def fileOrDirectory(d):

   f = open('/Users/axsandlin/workspaces/python/mp3_list','w')

   my_list = os.listdir(d)

   for x in my_list:
         
      if os.path.isfile(d + '/' + x):
         print "File:", x
         f.write(x + '\n') 
      else:
         print "Directory:", x
 
   f.close()

#call my method and pass it a directory.

fileOrDirectory(music_dir)


