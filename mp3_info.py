#!/usr/bin/python

#This is my first python script to read the id3 tags from mp3 files and export them to a JSON file.

#Aubri Sandlin

#Feb. 02, 2014


#This import is to work with files and directories.

import os
import json
import eyeD3

music_dir = "/Volumes/music/unsorted"

#method for determining if object in path passed in is a file or directory.

def getEyeD3Info(d):
#open file
#   f = open('/Users/axsandlin/workspaces/python/mp3_list','w')
   
#returns a list of the directory
   music_list = os.listdir(d)
   
   type = ""
   json_string = ""
   
   for x in music_list:
      
#checks to see if directory object is a file       
      if os.path.isfile(d + '/' + x):
         type = "file" 
      else:
         type = "dir"
      
      json_string = json.dumps({'type': type, 'name': x}, sort_keys=True,
                                    indent=4, separators=(',', ': '))
     
      print json_string
#      f.write(json_string)
      
#close file
#  f.close()
   
   for x in music_list:  
      
      if os.path.isfile(d + '/' + x):
      
         if eyeD3.isMp3File(d + '/' + x):
            
            tag = eyeD3.Tag()
            tag.link(d + '/' + x)
                    
            print "Artist: ", tag.getArtist()
            print "Album: ", tag.getAlbum()
            print "Title: ", tag.getTitle()
            print "Genre: ", str(tag.getGenre())
            print "Track #", tag.getTrackNum()
            
      
         else:
            print "Not an MP3"
       
   
#call my method and pass it a directory.
getEyeD3Info(music_dir)


#{
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
#      }
#}
   
      
      
