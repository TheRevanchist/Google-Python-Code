#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

def helpCreateDic(filename):
# this is a helper function which reads a file, and then creats a dictionary
# which as a key has a word, while as value the number of occurrences of that
# word in the text    
    
  # read the file and split it by word   
  f = open(filename, 'r') 
  text = f.read()
  dic = {}
  
  # if word is not in dictionary, put it there, otherwise just increase its 
  # occurrences by 1
  for word in text.split():
    lowerCaseWord = word.lower()
    if lowerCaseWord not in dic:  
      dic[lowerCaseWord] = 1
    else:
      dic[lowerCaseWord] += 1
  return dic    
      
def print_words(filename):
  
  # call the helper function to get the dictionary
  dic = helpCreateDic(filename)
      
  # print the results in sorted order by key    
  for key in sorted(dic):
    print key, dic[key] 
    
def print_top(filename):    
                    
  # call the helper function to get the dictionary
  dic = helpCreateDic(filename)
  i = 0
  
  # iterate in a dictionary which is sorted by value
  for word in sorted(dic, key = dic.get, reverse = True):
    if i < 20:
      print word, dic[word]
      i += 1
    else:
      break   

# Changed the main function in order to be able to run it from an IDE
def main():
  
  filename = "D:/Workbench/Online Courses/Google Python Class/google-python-exercises/basic/alice.txt"
  print_words(filename)
  print ''
  print ''
  print ''
  print_top(filename)

if __name__ == '__main__':
  main()
