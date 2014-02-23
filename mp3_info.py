#!/usr/bin/python

#This is my first python script to read the id3 tags from mp3 files and export them to a JSON file.

#Aubri Sandlin

#Feb. 02, 2014


#This import is to work with files and directories.

import os
import json
import eyeD
from argparse import ArgumentParser3

#import JSON
music_dir = "/Volumes/music/sorted/Styx"

folders = {}
switch = 0

def getEyeD3Info(d, songs):
   #print("getEyeD3Info(" + d + ", songs)")
   music_list = os.listdir(d)
   
   type = ""
   json_string = ""
   json_txt = ""
   dirsongs = []
   
   for x in music_list:
      file = d + "/" + x
      if os.path.isdir(file):
         #print file + " is dir"
         songs.append(dict(folder=file, songs=getEyeD3Info(file, songs)))
         print len(songs)
      #   return songs.append(dir_data)
      elif os.path.isfile(file):   
         #print "---------------------"
         #print file
         #print "---------------------"
         if eyeD3.isMp3File(file):
            if not (x.startswith('.')):
            # Look up Regular Expressions (regex).
            # Put an if condition here which checks the name of the file (x) 
            #    if it starts with a dot (.), do not do the tasks below (ignore the file).            
               #print file + " is mp3"
               tag = eyeD3.Tag()
               tag.link(file) 
               song = {
                  'file_name': x, 
                  'artist' : tag.getArtist(), 
                  'album': tag.getAlbum(), 
                  'title': tag.getTitle(), 
                  'genre': str(tag.getGenre()), 
                  'track': tag.getTrackNum()
               }

               dirsongs.append(song)
               #print song
   entry = {}
   entry['folder'] = d
   entry['songs'] = dirsongs
   songs.append(entry)
      #songs.update(dict(folder=file, songs=dirsongs))
      #print "dirsongs = " + str(len(songs))
               #print d
   return songs
      
   
  
   
#call my method and pass it a directory.

songs = []
dir_eyed3_data = getEyeD3Info(music_dir, songs)

#print json.dumps(dir_eyed3_data, sort_keys=True, indent=2, separators=(',', ': '))
#workspace_dir = os.getenv("WORKSPACE")   
print(dir_eyed3_data)
print "--------------------------"
print(str(dir_eyed3_data))
#JSON.stringify(dir_eyed3_data, null, 4);
f = open("./output.json", "w")
json.dump(dir_eyed3_data, f)

#f.seek(0)
#f.write(str(dir_eyed3_data))
f.close
#f.write(json.dumps(dir_eyed3_data, sort_keys=True, indent=2, separators=(',', ': ')))

#{  {
#   folder: "/Volumes/music/unsorted",
#   songs:
#      {
#         {
#            file_name: "08_-_Get_lucky.mp3",
#            artist: "Daft Punk",
#            album: "Random Access Memories",
#            title: "Get Lucky"
#            genre: "funk",
#            track: "08"
#         },
#         {
#            file_name: "09_-_Beyond.mp3",
#            artist: "Daft Punk",
#            album: "Random Access Memories",
#            title: "Beyond"
#            genre: "funk",
#            track: "09"
#         },
#         {
#            file_name: "Energy_Meditation_-_Self-Hypnosis.mp3",
#            artist: "",
#            album: "",
#            title: ""
#            genre: "",
#            track: ""
#         }
#      },
#   }
#   {
#   folder: "/Volumes/music/sorted",
#   songs:
#      {
#         {
#            file_name: "08_-_Get_lucky.mp3",
#            artist: "Daft Punk",
#            album: "Random Access Memories",
#            title: "Get Lucky"
#            genre: "funk",
#            track: "08"
#         },
#         {
#            file_name: "09_-_Beyond.mp3",
#            artist: "Daft Punk",
#            album: "Random Access Memories",
#            title: "Beyond"
#            genre: "funk",
#            track: "09"
#         },
#         {
#            file_name: "10_-foobar.mp3",
#            artist: "Daft Punk",
#            album: "Random Access Memories",
#            title: "Get Lucky"
#            genre: "funk",
#            track: "10"
#         }
#      }
#   }
#}
   
      
      
