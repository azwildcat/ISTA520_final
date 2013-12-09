# version 2

#!/usr/bin/python

# This script creates a Makeflow file based on the number of images inside a specified directory 
# and a desired amount of partitions. The created Makeflow file will call extract_keypoints.py
# to process the images
# Input: See print_usage() for the input parameters and their order.
# Output: a single Makeflow file
# Author: Ian Montgomery and Jorge Rodriguez



import os
import sys
import glob

cmd = "../vlfeat-0.9.17/bin/glnxa64/sift"

num_args = 2

def print_usage():
    print "Usage: python ", sys.argv[0], " <images_directory> <number_of_partitions>"
    sys.exit(1)

if (len(sys.argv) == 1):
    print_usage()
elif len(sys.argv) <> num_args:
    print "The script expects %d arguments. You provided %d." % (num_args, len(sys.argv))
    print_usage()




if len(sys.argv) > 1:
	path_in = sys.argv[1]
	if os.path.isdir(path_in) == False:
		print("Not a Valid directory:  Exiting")
		quit()
#	n = len(glob.glob1(path_in, '*.pgm'))
	if len(sys.argv) > 2:
		if sys.argv[2].isdigit() == True:
			n = int(sys.argv[2])
		else:
			print "Input 2 is not a valid number: Exiting"
			quit()

else:
	print "No Path entered.  Exiting..."


if os.path.isdir(path_in + '/out_put/') == False:
	os.system('mkdir ' + path_in + '/out_put')
	print "Creating directory " + path_in + '/out_put'

num_files = len(glob.glob1(path_in,'*.pgm'))

num_part = num_files/n
rem_part = num_files%n

#print num_part
#print rem_part

images = glob.glob1(path_in,'*pgm')
#print images
print num_files

myfile = open('Makeflow','w')


'''
for image in images:

        myfile.write(path_in + "/" + image)
        myfile.write(" ")
myfile.write(cmd + ":")
myfile.write('\n'+'\n')
'''



for part in range(num_part):
        myfile.write('x' + str(part) +":" + "extract_keypoints.py\n")
        myfile.write("  python extract_keypoints.py " + path_in + " " + str(part) + ' ' + str(n) + " > " + "x" + str(part) + "\n")

if rem_part > 0:
	myfile.write('x' + str(part+1) +":" + "extract_keypoints.py\n")
	myfile.write('  python extract_keypoints.py ' + path_in + " " + str(part + 1) + ' ' + str(rem_part) + ' ' + str(n) + " > " + 'x' + str(part+1) + '\n')
myfile.close()


