#!/usr/bin/python

#This is my first python script to read the id3 tags from mp3 files and export them to a JSON file.

#Aubri Sandlin

#Feb. 02, 2014


#This import is to work with files and directories.

import os
import json
import eyeD3

music_dir = "/Volumes/music/unsorted/Passion_Pit/Passion_Pit_-_Gossamer_mp3/"

#method for determining if object in path passed in is a file or directory.

folders = {}
def getEyeD3Info(d):
   songs = []
   music_list = os.listdir(d)
   
   type = ""
   json_string = ""
   json_txt = ""
   for x in music_list:  
      if os.path.isfile(d + '/' + x):
         if eyeD3.isMp3File(d + '/' + x):
            
            print d + '/' + x + " is mp3"
            tag = eyeD3.Tag()
            tag.link(d + '/' + x) 
            song = {
               'file_name': x, 
               'artist' : tag.getArtist(), 
               'album': tag.getAlbum(), 
               'title': tag.getTitle(), 
               'genre': str(tag.getGenre()), 
               'track': tag.getTrackNum()
            }
            songs.append(song)
   dir_data = {'folder': d, 'songs': songs}
   return dir_data
   
#call my method and pass it a directory.
dir_eyed3_data = getEyeD3Info(music_dir)

print json.dumps(dir_eyed3_data, sort_keys=True, indent=2, separators=(',', ': '))
   


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
#}
   
      
      
