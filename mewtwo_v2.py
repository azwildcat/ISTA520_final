# version 2
import os
import sys
import glob

cmd = "../vlfeat-0.9.17/bin/glnxa64/sift"

if len(sys.argv) > 1:
	path_in = sys.argv[1]
	if os.path.isdir(path_in) == False:
		print("Not a Valid directory:  Exiting")
		quit()
	n = len(glob.glob1(path_in, '*.pgm'))
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

for image in images:

        myfile.write(image)
        myfile.write(" ")
myfile.write(cmd + ":")
myfile.write('\n'+'\n')

for part in range(num_part):
        myfile.write('x' + str(part) +":" + "final_test_v5.py\n")
        myfile.write("  python final_test_v5.py " + path_in + " " + str(part) + ' ' + str(n) + " > " + "x" + str(part) + "\n")

if rem_part > 0:
	myfile.write('x' + str(part+1) +":" + "final_test_v5.py\n")
	myfile.write('  python final_test_v5.py ' + path_in + " " + str(part + 1) + ' ' + str(rem_part) + ' ' + str(n) + " > " + 'x' + str(part+1) + '\n')
myfile.close()

