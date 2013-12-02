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

t = 0
n = 1
if len(sys.argv) > 1:
	path_in = sys.argv[1]
	if os.path.isdir(path_in) == False:
		print("Not a valid directory:  Exiting")
		quit()
	
	numb = len(glob.glob1(path_in,'*.pgm'))

	if len(sys.argv) > 2:
		if sys.argv[2].isdigit() == True:
			n = int(sys.argv[2])
		else:
			print "Input 2 is not a valid number:  Exiting"
			quit()
		if len(sys.argv) > 3:
			if sys.argv[3].isdigit() == True:
				t = int(sys.argv[3])
				numb = t
			else:
				print "Input 3 is not a valid number:  Exiting"
				quit()

			if len(sys.argv) > 4:
				if sys.argv[4].isdigit() == True:
					numb = int(sys.argv[4])
				else:
					print "Input 4 is not a valid number: Extiging"
					quit()
else:
	print "No path entered.  Exiting..."
	quit()

if os.path.isdir(path_in + '/out_put') == False:
	os.system('mkdir ' + path_in + '/out_put')
	print "Creating directory " + path_in + '/out_put'
path_out = path_in + '/out_put/' 				#where we want the output to go

num_files = len(glob.glob1(path_in,'*.pgm'))		#number of file of type
start_val = n * numb
end_val = start_val + t

img_names = []
for f in range(start_val,end_val):
	 img_names.append('%6.6i' % f + '.pgm')	#tells up what the names of each file we are using stored as an array
img_count = len(img_names) 				#tells us how many images there are

print img_names

#print "%02d" % (t)  used for debug

if __name__ == '__main__':
	jobs = []
	for i in range(0,img_count):
		key_file = path_out + img_names[i].replace('.pgm','')  +'.vl'
		cmd = '~/vlfeat-0.9.17/bin/glnxa64/sift' + " " + path_in + "/"  +img_names[i] + " -o " + key_file
		p = multiprocessing.Process(target=worker, args=(cmd, img_names[i]))	
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
