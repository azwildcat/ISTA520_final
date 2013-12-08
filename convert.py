# this script uses the convert function of imagemagik
# to mass convert color .jpg images to black and white
# .pgm files and changes the change permission to 755
# so that the images can be used for swift keypoint
# extraction.
# input: < ./ directory containing images >
# Out put: .pgm file
#Auther:  Ian Montgomery (ianmonty@email.arizona.edu)

import os
import sys
import multiprocessing


#print multiprocessing.cpu_count()
path = sys.argv[1]
os.chdir(path)
cmd = 'for x in `ls *.jpg`; do convert $x ${x%.*}.pgm; done'
print cmd
os.system(cmd)
cmd = 'for x in `ls *.pgm`; do chmod -c 755 $x; done'
print cmd
os.system(cmd)
os.chdir('..')
