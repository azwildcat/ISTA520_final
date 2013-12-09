#!/usr/bin/python

# This script uses the multiprocess module to
# distribut a sift extraction processes across
# the cores of a worker node.  
# Input: <directory path to data> <start value> <end value>
# Output: corresponding .vl file with sift data in directory
# <path to data/out_put
# to change number of workers, change core_worker variable to
# a different number
# Author Ian Montgomery (ianmonty@email.arizona.edu)

import os
import sys
import glob
import multiprocessing

##Worker used to submit to differenct cores of 
def worker(job_queue):
	"""Worker function"""
	for ctrl in iter(job_queue.get, 'STOP'):
		print ctrl
		error_code = os.system(ctrl)
		if (error_code <> 0):
			raiseException("ERROR: SIFT didn't run correctly")
			print "Terminating process"
			sys.exit(1)


path_in = sys.argv[1]
path_out = path_in + '/out_put/'

start_time = int(sys.argv[2])+1
end_time = int(sys.argv[3])+1

# number of mutliprocess threads performing tasks.  be careful no to exceed the capacity of
# the system.  Number of workers greater than 10 seems to have minial increase in speed
core_worker = 22

if __name__ == '__main__':
	job_queue = multiprocessing.Queue()
	for i in range(start_time,end_time):
		key_file = path_out + '%6.6i' % i  +'.vl'
		cmd = 'sift' + " " + path_in + "/"  + '%6.6i' % i + '.pgm' + " -o " + key_file
		job_queue.put(cmd)
	
	#Setup workers to work on queue	
        workers = [multiprocessing.Process(target=worker, args=(job_queue,)) for i in range(core_worker)]
	
	#stop flag for workers, needs to be equivalent to the number of workers else system hangs
	for i in range(core_worker):
		job_queue.put('STOP')
	
	#starts workers
	for each in workers:
		each.start()



# v8    optimized for different systems to ensure no overloading by use of queue/worker
# 	system.
#
#
# v7	redacted
#
# v6 	redisiged to work with makeflow
#	known issue, nut sure how to allow "user defined" file named size
#	
# v5	allow for user defined paths at command line, added input error management 
#	rearranged order of number of partiions and partition number
#	checks for/creates out_put directory inside input directory

# v4 	added multiprocessing to access multiple cores

# v3 	updated system to take specify which numeric files for better compatablility with
#    	distributed systems

# v2 	updated program so that all files of given type can be read in for use

# v1 	program tested working

# Coded by Ian Montgomery with help from Kate Kharitonova.  Designed for ISTA 420/520, Applied Cyberinfrastructer Concepts
# ISTA 420/520 Final Project
