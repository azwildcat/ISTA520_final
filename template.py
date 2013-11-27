ISTA520_final
=============

#!/usr/bin/python

# This script uses prism.py functions to compute gravity for
# a single point whose data is provided on the command line.
# Input: See print_usage() for the input parameters and their order.
# Output: a single file that with one line containing the
# position ID, timestep and gravity measurement.
# Author: Yekaterina Kharitonova (ykk-at-email.arizona)

import sys
from prism import calc_prism, calc_macmillan, calc_pointmass
from math import sqrt, pow

num_args = 6 # including the script name

def print_usage():
    print "Usage: python ", sys.argv[0], " <density_grid_file> ID X Y Z"
    sys.exit(1)

if (len(sys.argv) == 1):
    print_usage()
elif len(sys.argv) <> num_args:
    print "The script expects %d arguments. You provided %d." % (num_args, len(sys.argv))
    print_usage()


Example output:

$ python grav_per_point.py
Usage: python  grav_per_point.py  <density_grid_file> ID X Y Z

$ python grav_per_point.py density_grid.txt 1 200 200
The script expects 6 arguments. You provided 5.
Usage: python  grav_per_point.py  <density_grid_file> ID X Y Z
