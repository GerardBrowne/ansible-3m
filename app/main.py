#!/usr/bin/python

import sys

str1=sys.argv[1]
str2=sys.argv[2]

def isAnagram (str1, str2) -> bool:
  print(str1)
  # sanitize inputs
  str1 = str1.lower()
  str2 = str2.lower()

  if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        return True
    else:
        return False
  else:
    False
