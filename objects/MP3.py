#!/usr/bin/python

#Aubri Sandlin

#Feb. 25, 2014

#This is a MP3 objects.

import eyeD3
import logging
import json

class MP3:
   
   artist = None
   album = None
   title = None
   genre = None
   track_num = None
   filepath = None
   tag_info = {}
   
   
   
   def __init__(self, d, logging):
     
      self.filepath = d
      self.logging = logging
      return None
   
   
   def getTagInfo(self):
      
   
      tag = eyeD3.Tag()
      tag.link(self.filepath) 
      self.artist = tag.getArtist(), 
      self.album = tag.getAlbum(), 
      self.title = tag.getTitle(), 
      self.genre = str(tag.getGenre()), 
      self.track_num = tag.getTrackNum()


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
      
 
