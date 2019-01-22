import filefinder as ff
from os import system

# Get list of all job script files in directory

jobfilelist = ff.find_sorted_local_input_fileset("job_*")

nfiles = len(jobfilelist)

print "There are ", nfiles, " files"

# Submit each job using sbatch

for jobfile in jobfilelist:

	command = "sbatch "+jobfile

	print command
	system(command)
	



