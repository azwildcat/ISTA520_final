# This script uses the `convert` utility of Imagemagik
# to convert color .jpg images to grey scale .pgm files.
# Input: < path to directory with images >
# Output: .pgm file
# Author:  Ian Montgomery (ianmonty@email.arizona.edu)

import os
import sys
import multiprocessing

debug = 1 # whether or not to print commands

#print multiprocessing.cpu_count()
path = sys.argv[1]
os.chdir(path)
#cmd = 'for x in `ls *.jpg`; do convert $x ${x%.*}.pgm; done'

if os.path.isdir('../pgm') == False: 
    os.mkdir('../pgm')
cmd = 'for x in `ls *.jpg`; do convert $x ../pgm/${x%.*}.pgm; done'
if debug: print cmd
os.system(cmd)
"""
cmd = 'for x in `ls *.pgm`; do chmod -c 755 $x; done'
print cmd
os.system(cmd)
os.chdir('..')
"""
