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
#open file
#   f = open('/Users/axsandlin/workspaces/python/mp3_list','w')
   
#returns a list of the directory
   music_list = os.listdir(d)
   
   type = ""
   json_string = ""
   
#   for x in music_list:
      
#checks to see if directory object is a file       
#      if os.path.isfile(d + '/' + x):
#         type = "file" 
#      else:
#         type = "dir"
#      
#      json_string = json.dumps({'type': type, 'name': x}, sort_keys=True,
 #                                   indent=4, separators=(',', ': '))
     
      #print json_string
#      f.write(json_string)
      
#close file
#  f.close()
   json_txt = ""
   for x in music_list:  
      if os.path.isfile(d + '/' + x):
         if eyeD3.isMp3File(d + '/' + x):
            
            print d + '/' + x + " is mp3"
            tag = eyeD3.Tag()
            tag.link(d + '/' + x) 
            #print tag
            #print tag.getTitle()
            #print tag.getArtist()
            #print tag.getAlbum()
            song = {
               'file_name': x, 
               'artist' : tag.getArtist(), 
               'album': tag.getAlbum(), 
               'title': tag.getTitle(), 
               'genre': str(tag.getGenre()), 
               'track': tag.getTrackNum()
            }
            songs.append(song)
            
            #json_txt = json.load(
            #                  {
            #                     'folder': d
            #                     , 
            #                     'songs':  
            #                        [
            #                           {
            #                              'name': x,
            #                              #'file_name': tag.getTitle(), 
            #                              #'artist' : tag.getArtist(), 
            #                              #'album': tag.getAlbum(), 
            #                              #'title': tag.getTitle(), 
            #                              #'genre': str(tag.getGenre()), 
            #                              #'track': tag.getTrackNum()
            #                           },
            #                        ]
            #                  }
            #                )
         #else:
         #   print "Not an MP3 -> " + d + '/' + x 
   #print json.encode(songs)
   
   dir_data = {'folder': d, 'songs': songs}
   print json.dumps(dir_data, sort_keys=True, indent=2, separators=(',', ': '))
   #json.dumps(json_txt, sort_keys=True,
   #   indent=3, separators=(',', ' : '))
#print json.dumps({'4': 5, '6': 7}, sort_keys=True,
#                    indent=4, separators=(',', ': '))  

#{
#    "4": 5,
#    "6": 7
#}

#json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))
#'[1,2,3,{"4":5,"6":7}]'   
   

   
   
#call my method and pass it a directory.
getEyeD3Info(music_dir)


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
   
      
      
