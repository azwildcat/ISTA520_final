# version 2
import os
import sys
import glob

cmd = "sift"

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

file_names = glob.glob1(path_in, '*.pgm')
num_files = len(file_names)

num_part = num_files/n
rem_part = num_files%n

#print num_part
#print rem_part

for i in range(0,num_part):
	os.system('mkdir ' + path_in + '/data' + '%4.4i' % i)
	beginning = (n * i)+1
	ending = beginning + n -1
	print beginning
	print ending
	for j in range(beginning, ending):
		os.system('cp ' + path_in + '/' + '%6.6i' % j + '.pgm' + ' ' + path_in + '/data' + '%4.4i' % i)
	
	os.system('tar cvfj ' + 'data' + '%4.4i' %i + '.tar.tbz ' + path_in + '/data' + '%4.4i' % i)
	os.system('iput data' + '%4.4i'	% i + '.tar.tbz') 
	os.system('rm ' + path_in + '/data' + '%4.4i' %i + '/*.pgm')
	os.system('rmdir ' + path_in + '/data' + '%4.4i' % i)
print num_files

if rem_part > 0:
	num_part
	os.system('mkdir ' + path_in + '/data' + '%4.4i' % num_part)
        beginning = (n * num_part)+1
        ending = beginning +  rem_part
        print beginning
        print ending
	for j in range(beginning, ending):
                os.system('cp ' + path_in + '/' + '%6.6i' % j + '.pgm' + ' ' + path_in + '/data' + '%4.4i' % num_part)

        os.system('tar cvfj ' + 'data' + '%4.4i' % num_part + '.tar.tbz ' + path_in + '/data' + '%4.4i' % num_part)
	os.system('iput data' + '%4.4i' % num_part + '.tar.tbz')
	os.system('rm ' + path_in + '/data' + '%4.4i' %num_part + '/*.pgm')
        os.system('rmdir ' + path_in + '/data' + '%4.4i' % num_part)

myfile = open('Makeflow','w')


myfile.write('final_test_v6.py')
myfile.write(" ")
myfile.write(cmd + ":")
myfile.write('\n'+'\n')

for part in range(num_part):
        myfile.write('x' + str(part) +":" + "final_test_v6.py\n")
        myfile.write("  python final_test_v6.py " + path_in.replace('.', '') + " " + str(part) + ' ' + str(n) + " > " + "x" + str(part) + "\n")

if rem_part > 0:
	myfile.write('x' + str(part+1) +":" + "final_test_v6.py\n")
	myfile.write('  python final_test_v6.py ' + path_in.replace('.','') + " " + str(part + 1) + ' ' + str(rem_part) + ' ' + str(n) + " > " + 'x' + str(part+1) + '\n')
myfile.close()


