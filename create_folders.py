import filefinder as ff
from os import system

# Get list of all directories

paramfilelist = ff.find_sorted_local_input_fileset("*.params")

nfiles = len(paramfilelist)

print "There are ", nfiles, " files"

# for blocks of 500, create a folder and move them

ifile = 0
inext = 0
current_dir = ""

for ifile in range(nfiles):

	if ifile==inext:
		inext = inext+500
		current_dir = "run_to_"+str(inext)

		# Create new directory
		command ="mkdir "+current_dir
		print command
		system(command)

		# Copy essential executable files

		command = "cp job-placeholder " +current_dir
		print command
		system(command)
		command = "cp nbody_hermite " +current_dir
		print command
		system(command)

	# Now move each parameter file

	command = "mv "+str(paramfilelist[ifile])+" "+current_dir
	print command
	system(command)
	



