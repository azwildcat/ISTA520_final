#!/usr/bin/env python

from work_queue

import * import sys

print "Listening on port %d." % Q.port

infile_array = ["othello.txt", "macbeth.txt", "kinglear.txt", "juliuscaesar.txt", "hamlet.txt"]
#num_tasks = 5
num_tasks = len(infile_array)
print "Submitting " + str(num_tasks) + " simulation tasks..."
for i in range(0, num_tasks):
    infile = infile_array[i]
    outfile = "out." + infile
    command = "python shakespeare-compare.py %s > %s" % (infile, outfile)

    T = Task(command)

    T.specify_file("shakespeare-compare.py", "shakespeare-compare.py", WORK_QUEUE_INPUT)
    T.specify_file(infile, infile, WORK_QUEUE_INPUT)
    T.specify_file(outfile, outfile, WORK_QUEUE_OUTPUT)
print "Done."

print "Waiting for tasks to complete..."
while not Q.empty():
    T = Q.wait(5)
    if T:
        print "Task (id# %d) complete: %s (return code %d)" % (T.id, T.command, T.return_status)

print "All done."

