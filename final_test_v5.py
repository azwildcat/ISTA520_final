# Version 5 -beta
# this version is still a little buggy, I want to try it on a different machine with.
# command:  $ python final_test_v[x] [path_in] [number of partitions] [partition number]

import os
import sys
import glob
import multiprocessing

##Worker used to submit to differenct cores of 
def worker(ctrl, name):
	"""Worker function"""
#	print ctrl
	error_code = os.system(ctrl)
	if (error_code <> 0):
		raiseException("ERROR: SIFT didn't run correctly on " + name)
		print "Terminating process"
		sys.exit(1)
	return

t = 0
n = 1
if len(sys.argv) > 1:
	path_in = sys.argv[1]
	if os.path.isdir(path_in) == False:
		print("Not a valid directory:  Exiting")
		quit()

	if len(sys.argv) > 2:
		if sys.argv[2].isdigit{} == True:
			t = int(sys.argv[2])
		else:
			print "Input 2 is not a valid number:  Exiting"
			quit()
		if len(sys.argv) > 3:
			if sys.argv[3].isdigit() == True:
				n = int(sys.argv[3])
			else:
				print "Input 3 is not a valid number:  Exiting"
				quit()
else:
	print "No path entered.  Exiting..."
	quit()

if os.path.isdir(path_in + '/out_put') == False:
	os.system('mkdir ' + path_in + '/out_put')
	print "Creating directory " path_in + '/out_put'
path_out = path_in + '/out_put/' 				#where we want the output to go

num_files = len(glob.glob1(path_in,'*.pgm'))		#number of file of type
num_in_div = num_files/n				#number of file per division
if num_in_div == 0:					#catch if num_in_div == 0
	num_in_div = num_files + 1

re_in_div = num_files%n					#number of remainder


start_val = t * num_in_div				#calc start position of array
if (start_val + num_in_div) <= num_files:
	end_val = start_val + num_in_div		#if will not go out of bounds
else:
	end_val = start_val + re_in_div			#if iteration will hit upper limit
	print end_val

img_names = glob.glob1(path_in,'*.pgm')[start_val:end_val] 	#tells up what the names of each file we are using stored as an array
img_count = len(img_names) 				#tells us how many images there are


#print "%02d" % (t)  used for debug

if __name__ == '__main__':
	jobs = []
	for i in range(0,img_count):
		key_file = path_out + img_names[i].replace('.pgm','')  +'.vl'
		cmd = '~/vlfeat-0.9.17/bin/glnxa64/sift' + " " + path_in + img_names[i] + " -o " + key_file
		p = multiprocessing.Process(target=worker, args=(cmd, img_names[i]))	
		jobs.append(p)
		p.start()

# v5	allow for user defined paths at command line, added input error management 
#	rearranged order of number of partiions and partition number
#	checks for/creates out_put directory inside input directory

# v4 	added multiprocessing to access multiple cores

# v3 	updated system to take specify which numeric files for better compatablility with
#    	distributed systems

# v2 	updated program so that all files of given type can be read in for use

# v1 	program tested working
