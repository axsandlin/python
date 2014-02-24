#!/usr/bin/python

#This is my first python script to read the id3 tags from mp3 files and export them to a JSON file.

#Aubri Sandlin

#Feb. 02, 2014


#This import is to work with files and directories.
import sys
import os
import json
import eyeD3
from argparse import ArgumentParser

#import JSON

def getEyeD3Info(current_dir, songs):
   
   print("getEyeD3Info(" + current_dir + ", songs)")
   dir_contents = os.listdir(current_dir)
   
   to_return = {}
   to_return["songs"] = []
   to_return["folders"] = []
   #
   # Iterate over dir contents & generate 2 lists. music_list && dir_list
   # Then iterate over each of these lists. 
   # For each music list, append to songs array.
   # For each dir list, call getEyeD3Info & append to list. (recursion)
   #
   subfolder_list = []
   subfile_list = []
   for x in dir_contents:
      x_full_path = current_dir + "/" + x
      if os.path.isdir(x_full_path):
         subfolder_list.append(x_full_path)
         #print("------- " + x)
      elif os.path.isfile(x_full_path) and not (x.startswith(".")) and eyeD3.isMp3File(x_full_path):
         subfile_list.append(x)
   
   # I know have a list of files and dirs. 
   #sys.exit(1)
   
   # Now it"s time to do directories. This is where recursion will come in.
   for d in subfolder_list:
      folder = {
         "folder_name": d,
         "contents": getEyeD3Info(d, songs)
      }
      to_return["folders"].append(folder)  

   # Create a collection of song dictionaries.
   subfolder_song_list = []
   for f in subfile_list:
      try:
         tag = eyeD3.Tag()
         tag.link(current_dir + "/" + f) 
         song = {
            "file_name": f, 
            "artist" : tag.getArtist(), 
            "album": tag.getAlbum(), 
            "title": tag.getTitle(), 
            "genre": str(tag.getGenre()), 
            "track": tag.getTrackNum()
         }
      except:
         print "This is the mp3 causing the error: " + (current_dir + "/" + f)
         
         
      
      subfolder_song_list.append(song)
   to_return["songs"] = subfolder_song_list
   
   return to_return
   
parser = ArgumentParser(description="""***Get all resources required.""")
parser.add_argument('--dir', help="The directory you want to scan", default="/Users/axsandlin/Music")
args = parser.parse_args()

if not os.path.isdir(args.dir):
   print "Error: " + args.dir + "is not a directory"
   sys.exit(1)
else:
   songs = {}
   songs["folder_name"] = args.dir
   dir_eyed3_data = getEyeD3Info(args.dir, songs)
   
   f = open("./output.json", "w")
   json.dump(dir_eyed3_data, f)
   f.close

