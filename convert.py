import os
import sys
import multiprocessing


print multiprocessing.cpu_count()
path = sys.argv[1]
os.chdir(path)
cmd = 'for x in `ls *.jpg`; do convert $x ${x%.*}.pgm; done'
print cmd
os.system(cmd)
cmd = 'for x in `ls *.pgm`; do chmod -c 755 $x; done'
print cmd
os.system(cmd)
os.chdir('..')
