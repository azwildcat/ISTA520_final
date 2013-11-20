import os
import glob

path_in = './slide_img/'  				# where the home images are
path_out = './slide_img_out/' 				#where we want the output to go
img_names = (glob.glob1(path_in,'*.pgm')) 		#tells up what the names of each file we are using stored as an array
img_count = len(img_names) 				#tells us how many images there are


for i in range(0,img_count):
	key_file = path_out + img_names[i].replace('.pgm','')  +'.vl'
	cmd = '~/vlfeat-0.9.17/bin/glnxa64/sift' + " " + './slide_img/' + img_names[i] + " -o " + key_file
	print cmd
	error_code = os.system(cmd)
	if (error_code <> 0):
        	raise Exception("ERROR: SIFT didn't run correctly on 001.pgm")
        	print "Terminating process."
        	sys.exit(1)
