import glob

cmd = "../vlfeat-0.9.17/bin/glnxa64/sift"
path_in = './slide_img/'
num_files = len(glob.glob1(path_in,'*.pgm'))

images = glob.glob1(path_in,'*pgm')
print images
print num_files

myfile = open('Makeflow','w')

for image in images:

        myfile.write(image)
        myfile.write(" ")
myfile.write(cmd + ":")
myfile.write('\n'+'\n')

for image in images:
        myfile.write(image[0:3] + ".vl: " + image + " " + cmd + '\n')
        myfile.write("  " + cmd + " " + image + " > " + image[0:3] + ".vl" + '\n')
myfile.close()
