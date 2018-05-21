#!/usr/bin/env python
from __future__ import print_function
import os, sys

path = './aggregate'

#if len(sys.argv) == 2:
#    path = sys.argv[1]

try:
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise

files = os.listdir('.')
for name in files:
    if "-" in (name[-23:-22]):
        print(name)
        output_file = path + '/' + name.split('-')[0]
        try:
            with open(name, 'r') as s, open(output_file, 'ab+') as d:
                content = s.read()
                d.write(content+'\n')
        except IOError:
            print("error opening ",name)
            continue