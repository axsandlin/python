#!/usr/bin/python

#Aubri Sandlin

#Feb. 25, 2014

#This is a MP3 objects.

import eyeD3
from mutagenwrapper import read_tags
from mutagen.mp3 import MP3
from objects import pygn
import logging
import json

class MP3Data:
   
   artist = None
   my_artist = None
   album = None
   my_album = None
   title = None
   genre = None
   track_num = None
   my_track_num = None
   disk_num = None
   filepath = None
   client_id = "12286976-F95C7AC0188B014B1DE8D336465F1CDB"
   user_id = "262426062807998760-B2D2FE37FD4EA1E96D6EDE4D1A6ED9C6"
   metadata = None
   metadata = None
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
       
       self.my_artist = mp3_info['artist']
       self.my_album = mp3_info['album']   
       self.my_title = mp3_info['title']
       self.my_genre = mp3_info['genre']
       self.my_track_num = mp3_info['tracknumber'] 
       self.my_disk_num = mp3_info.find('discnumber')
     
       
       tag_info_json = {
          
            "file_name": self.filepath, 
            "artist" : self.my_artist[0], 
            "album": self.my_album[0],
            "title": self.my_title[0], 
            "genre": self.my_genre[0], 
            "track": self.my_track_num[0],
            "disk": self.my_disk_num
        }
        
       print "**********************************************************"
        
       self.logging.debug("Song Info Mutagen=" + json.dumps(tag_info_json, sort_keys=True, indent=2, separators=(',', ': ')))
       self.query_gracenote()
   
   
            
   def get_userid_from_gracenote(self):
      
      #The user_ID needs to be stored in peristant storage (on the file system) and this request should only done once per application to avoid hitting your API quota.
      #You can then use the user_ID for subsequent pygn function calls.

      user_id = pygn.register(client_id)
      print "########################################"
      print user_id
      print "########################################"
      
   def query_gracenote(self):

      #The returned gnmetadata object is a Python dict containing multiple metadata fields.
      
      try:
         self.metadata = pygn.search(clientID=self.client_id, userID=self.user_id, artist=self.my_artist[0], album=self.my_album[0], track=self.my_track_num[0])
         print "#####################################################################################################"
         self.logging.debug("This is the info from gracenote:" + json.dumps(self.metadata, sort_keys=True, indent=2, separators=(',', ': ')))
         print "#####################################################################################################"
      
      except Exception, e:
         self.logging.debug("This is the error from gracenote:" + json.dumps(self.metadata, sort_keys=True, indent=2, separators=(',', ': ')))
         logging.exception(e)
     
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
      
 
