#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  
  # get the host
  underline = filename.index('_')
  host = filename[underline + 1:]
  
  # open the file and get all the urls which contain word 'puzzle'
  f = open(filename, 'r') 
  text = f.read()
  urls = re.findall(r'GET(\s\S+\puzzle\S+)', text)
  dic = {}
  for elem in urls:
    dic['http://' + host + elem[1:]] = 1
  print dic  
  return dic

def download_images(img_urls, dest_dir, index):#, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  dic = sorted(img_urls)
  listofImages = []
  for i in range(len(dic)):
    name = 'img' + str(i) + '.jpg'
    a = urllib.urlretrieve(dic[i], os.path.join(dest_dir, name))
    listofImages.append(a)
    print 'Downloading: ' + name
  
  # fill the index.html file     
  f = open(index, 'w')
  f.write('<html><body>\n')
  for elem in listofImages:
    f.write('<img src=' + elem[0][89:] + '>')
    #print '<img src=' + elem[0][89:] + '>'
  f.close()     
  

def main():
    
  # part A and B  
  filename = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/logpuzzle/animal_code.google.com"
  img_folder = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/logpuzzle/animal"
  index = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/logpuzzle/animal/index.html"
  listOfURLs = read_urls(filename)
  download_images(listOfURLs, img_folder, index)
  
  # part C
  # couldn't understund the instructions

if __name__ == '__main__':
  main()
