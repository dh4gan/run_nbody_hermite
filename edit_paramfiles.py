import filefinder as ff
from os import system

# Get list of all parameter files in directory

paramfilelist = ff.find_sorted_local_input_fileset("*.params")

nfiles = len(paramfilelist)

print "There are ", nfiles, " files"

# Create a new parameter file with a single adjusted parameter

for paramfile in paramfilelist:

	prefix = paramfile.split('.')[0]

	newparamfile = prefix+"_2e-3.params"

#	command = "sed  '6s/1.0e-5/2.0e-3/g' "+paramfile+" > "+newparamfile
	command = "sed -i '6s/1.0e-5/2.0e-3/g' "+paramfile
	print command
	system(command)
	



