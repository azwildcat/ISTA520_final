# Version 3
# command:  $ python final_test_v[x] [partition number] [number of partitions]

import os
import sys
import glob

t = 0
n = 1
if len(sys.argv) > 1:
	t = int(sys.argv[1])
	if len(sys.argv) > 2:
		n = int(sys.argv[2])


path_in = './slide_img/'  				# where the home images are
path_out = './slide_img_out/' 				#where we want the output to go

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

for i in range(0,img_count):
	key_file = path_out + img_names[i].replace('.pgm','')  +'.vl'
	cmd = '~/vlfeat-0.9.17/bin/glnxa64/sift' + " " + './slide_img/' + img_names[i] + " -o " + key_file
	print cmd
	error_code = os.system(cmd)
	if (error_code <> 0):
        	raise Exception("ERROR: SIFT didn't run correctly on " + img_name[i])
        	print "Terminating process."
        	sys.exit(1)

# v3 updated system to take specify which numeric files for better compatablility with
# distributed systems

# v2 updated program so that all files of given type can be read in for use

# v1 program tested working
