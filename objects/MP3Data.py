#!/usr/bin/python

#Aubri Sandlin

#Feb. 25, 2014

#This is a MP3 objects.

import eyeD3
from mutagenwrapper import read_tags
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import logging
import json

class MP3Data:
   
   artist = None
   album = None
   title = None
   genre = None
   track_num = None
   disk_num = None
   filepath = None
   tag_info = {}
   
   
   
   def __init__(self, d, logging):
     
      self.filepath = d
      self.logging = logging
      return None
   
   
   def get_tag_info_eyeD3(self):
      
      tag = eyeD3.Tag()
      tag.link(self.filepath) 
      self.artist = tag.getArtist(), 
      self.album = tag.getAlbum(), 
      self.title = tag.getTitle(), 
      self.genre = str(tag.getGenre()), 
      self.track_num = tag.getTrackNum()


   def get_tag_info_mutagen(self):
      
#Get mp3 info using the Mutagen Wrapper

       mp3_info = read_tags(self.filepath)
       
       my_artist = mp3_info['artist']
       my_album = mp3_info['album']   
       my_title = mp3_info['title']
       my_genre = mp3_info['genre']
       my_track_num = mp3_info['tracknumber'] 
       my_disk_num = mp3_info.find('discnumber')
     
       
       tag_info_json = {
          
            "file_name": self.filepath, 
            "artist" : my_artist[0], 
            "album": my_album[0],
            "title": my_title[0], 
            "genre": my_genre[0], 
            "track": my_track_num[0],
            "disk": my_disk_num
        }
        
       print "**********************************************************"
        
       self.logging.debug("Song Info Mutagen=" + json.dumps(tag_info_json, sort_keys=True, indent=2, separators=(',', ': ')))
   
   def load_info_from_gracenote(self):
      
      return None
            
   
 
   def log_object_info(self):
      
      self.tag_info = {
         
            "file_name": self.filepath, 
            "artist" : self.artist[0], 
            "album": self.album[0],
            "title": self.title[0], 
            "genre": self.genre[0], 
            "track": self.track_num[0]
         }
         
         
      self.logging.debug("Song Info=" + json.dumps(self.tag_info, sort_keys=True, indent=2, separators=(',', ': ')))
      
 
