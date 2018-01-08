# -*- coding: UTF-8 -*-
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

import re

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """

  f = open(filename)
  list = []
  year = []
  # TODO 优化做法：使用read()一次性读取文本，这样性能会更好
  for line in f.readlines():
    MatchObj = re.match(r'.*Popularity in (.*)</h3>', line)
    if MatchObj:
      year.append(MatchObj.group(1))

    # TODO 使用re.findall一次性获取匹配的字符串
    MatchObj = re.match(r'<tr align="right"><td>(.*)</td><td>(.*)</td><td>(.*)</td>', line)
    # TODO 抽取必要信息组成一个tuple，然后直接对tuple列表进行字符排序
    if MatchObj:
      list.append(MatchObj.group(2) + " " + MatchObj.group(1))
      list.append(MatchObj.group(3) + " " + MatchObj.group(1))

  list.sort()
  return year + list

def extract_names1(filename):
  f = open(filename, "r")
  text = f.read()

  names = []
  year_match = re.search(r'.*Popularity\sin\s(\d\d\d\d)', text)
  if year_match:
    year = year_match.group(1)
    names.append(year)
  else:
    sys.exit(1)

  rank_list = {}
  group = re.findall(r'<tr align="right"><td>(.*)</td><td>(.*)</td><td>(.*)</td>', text)
  for g in group:
    (rank, boyname, girlname) = g
    if boyname not in rank_list:
      rank_list[boyname] = rank
    if girlname not in rank_list:
      rank_list[girlname] = rank

  sorted_names = sorted(rank_list.keys())
  for name in sorted_names:
    names.append(name + " " + rank_list[name])

  return names

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names1(filename)
    names = "\n".join(names)

    if summary:
      f = open(filename + ".summary", "w")
      f.write(names)
      f.close()
    else:
      print names

if __name__ == '__main__':
   main()
