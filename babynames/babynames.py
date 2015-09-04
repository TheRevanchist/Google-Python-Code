#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  
  # read the text
  f = open(filename, 'r') 
  text = f.read()
  
  # find, extract and print the year 
  match = re.search(r'\w+\s\w+\s\d\d\d\d', text)
  print match.group()
  print ''
  
  # find all the names and their popularity
  tup = re.findall(r'(\d*)</td><td>+(\w+)</td><td>+(\w+)', text)
  
  # make a dic when as key are names, while as values are the name popularity
  dic = {}

  for elem in tup:      
    for i in range(1,3): 
    
      # if the name is alredy in the dictionary, then change the popularity 
      # value only if this version has a higher popularity (smaller number)
      if elem[i] in dic:
        if elem[0] < dic[elem[i]]:
          dic[elem[i]] = elem[0]
      # otherwise, just insert the new values
      else:
        dic[elem[i]] = elem[0]      
  return dic   

def helperFunc(dic, mainDic, year):
  # a helper function which creates a single dictionary from all the dictionaries
  # which are created seperately from each html file
      
  for key in dic:
    if key in mainDic:
      mainDic[key] += ['Year: ' + year + '   Popularity: ' + dic[key]]
    else:
      mainDic[key] = ['Year: ' + year + '   Popularity: ' + dic[key]]

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  
  # The main method has been completely changed in order to run it from IDE
  
  # For part A, just remove comments from lines 93 to 95
  # In console, you'll see the sorted results as required
  
  # For part B, just remove comments from lines 103 to 151
  # In line 148 you can change 'Samuel' to one of the other names  
  
  # Part A
  '''filename = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby1990.html"
  dic = extract_names(filename)
  for key in sorted(dic):
    print key, dic[key]'''
  
  # Part B
  filename1 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby1990.html"
  year1 = '1990'
  filename2 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby1992.html"
  year2 = '1992'
  filename3 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby1994.html"
  year3 = '1994'
  filename4 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby1996.html"
  year4 = '1996'
  filename5 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby1998.html"
  year5 = '1998'
  filename6 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby2000.html"
  year6 = '2000'
  filename7 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby2002.html"
  year7 = '2002'
  filename8 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby2004.html"
  year8 = '2004'
  filename9 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby2006.html"
  year9 = '2006'
  filename10 = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/babynames/baby2008.html"
  year10 = '2008'
  dic1 = extract_names(filename1)
  dic2 = extract_names(filename2)
  dic3 = extract_names(filename3)
  dic4 = extract_names(filename4)
  dic5 = extract_names(filename5)
  dic6 = extract_names(filename6)
  dic7 = extract_names(filename7)
  dic8 = extract_names(filename8)
  dic9 = extract_names(filename9)
  dic10 = extract_names(filename10)
  
  mainDic = {}    
      
  helperFunc(dic1, mainDic, year1)
  helperFunc(dic2, mainDic, year2)
  helperFunc(dic3, mainDic, year3)
  helperFunc(dic4, mainDic, year4)
  helperFunc(dic5, mainDic, year5)
  helperFunc(dic6, mainDic, year6)
  helperFunc(dic7, mainDic, year7)
  helperFunc(dic8, mainDic, year8)
  helperFunc(dic9, mainDic, year9)
  helperFunc(dic10, mainDic, year10) 
  
  try:
    for elem in mainDic['Joel']:
      print elem   
  except KeyError:
    print "The name you required isn't in top 1000 names in any of the years" 

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
