#!/bin/csh

U CAN SET A JOB NAME

#PBS -m bea

###CHANGE EMAIL ADDRESS
### Specify email address to use for notification.
#PBS -M ngizzi@email.arizona.edu

### List of PI groups available to each user can be found with "va" command
#PBS -W group_list=nirav

#PBS -q echo

#PBS -l jobtype=serial

#PBS -l select=1:ncpus=1:mem=1gb

#PBS -l place=pack:shared

#PBS -l walltime=01:00:00

#PBS -l cput=01:00:00

source /usr/share/Modules/init/csh
module load blas

###CHANGE DIRECTORY
### set directory for job execution, ~netid = home directory path
cd ~ngizzi/cctools-tutorial/hw1_part1

### run your executable program with begin and end date and time output
date
/usr/bin/time shakespear.py
date


