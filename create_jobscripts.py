import filefinder as ff
from os import system

# Get list of all parameter files in directory

paramfilelist = ff.find_sorted_local_input_fileset("*.params")

nfiles = len(paramfilelist)

print "There are ", nfiles, " files"

# Create a jobscript for each based on template jobscript

for paramfile in paramfilelist:

	prefix = paramfile.split('.')[0]

	jobfile = 'job_'+prefix

	command = "sed 's/placeholder/"+paramfile+"/g' job-placeholder > "+jobfile

	print command
	system(command)
	



