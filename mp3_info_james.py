#!/usr/bin/python

#This is my first python script to read the id3 tags from mp3 files and export them to a JSON file.

#Aubri Sandlin

#Feb. 02, 2014


#This import is to work with files and directories.
import sys
import os
import json
import eyeD3
from mutagen.easyid3 import EasyID3
import logging
from objects import MP3Data
from argparse import ArgumentParser

#import JSON

def getEyeD3Info(current_dir, songs, logging):
   
   
   logging.debug("getEyeD3Info(" + current_dir + ", songs)")
   
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
         "contents": getEyeD3Info(d, songs, logging)
      }
      to_return["folders"].append(folder)  

   # Create a collection of song dictionaries.
   
   subfolder_song_list = []
   
      
   for f in subfile_list:
      
      my_mp3 = MP3Data.MP3Data(current_dir + "/" + f, logging)
      
      try:
         my_mp3.get_tag_info_eyeD3()
         my_mp3.get_tag_info_mutagen()
         my_mp3.log_object_info()

         song = {
            "file_name": f, 
            "artist" : my_mp3.artist, 
            "album": my_mp3.album, 
            "title": my_mp3.title, 
            "genre": my_mp3.genre, 
            "track": my_mp3.track_num
         }
         
         subfolder_song_list.append(song)
      
      except Exception, e:
         logging.exception ("This is the mp3 causing the error: " + (current_dir + "/" + f))
         logging.exception(e)
         
         
   to_return["songs"] = subfolder_song_list
   
   return to_return
##############################################
# END OF METHOD DEF. START EXECUTION
##############################################

logging.basicConfig(level=logging.DEBUG)


parser = ArgumentParser(description="""***Get all resources required.""")
parser.add_argument('--dir', help="The directory you want to scan", default="/Users/axsandlin/Music")
args = parser.parse_args()

d = None
my_mp3_gn = MP3Data.MP3Data(d, logging)
#my_mp3_gn.get_userid_from_gracenote()

if not os.path.isdir(args.dir):
   print "Error: " + args.dir + " is not a directory"
   sys.exit(1)
else:
   songs = {}
   songs["folder_name"] = args.dir
   dir_eyed3_data = getEyeD3Info(args.dir, songs, logging)
   
   f = open("./output.json", "w")
   json.dump(dir_eyed3_data, f)
   f.close

  
