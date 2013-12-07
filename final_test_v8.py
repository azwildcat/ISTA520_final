# input design		>python final_test_v6.py [directory] [partition number] [number of files in current partition] [mode of files in partition // optional]
import os
import sys
import glob
import multiprocessing

##Worker used to submit to differenct cores of 
def worker(ctrl, name):
	"""Worker function"""
	print ctrl
	error_code = os.system(ctrl)
	if (error_code <> 0):
		raiseException("ERROR: SIFT didn't run correctly on " + name)
		print "Terminating process"
		sys.exit(1)
	return

path_in = sys.argv[1]
path_out = path_in + '/out_put/'

start_time = int(sys.argv[2])
end_time = int(sys.argv[3])

if __name__ == '__main__':
	jobs = []
	for i in range(start_time,end_time):
		key_file = path_out + '%6.6i' % i  +'.vl'
		cmd = '~/vlfeat-0.9.17/bin/glnxa64/sift' + " " + path_in + "/"  + '%6.6i' % i + '.pmg' + " -o " + key_file
		p = multiprocessing.Process(target=worker, args=(cmd, '%6.6i' % i + '.pgm'))	
		jobs.append(p)
		p.start()





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
