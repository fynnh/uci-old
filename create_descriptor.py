import json
import sys
import getopt

def saveDescriptor(version, dist, arch):
	with open('bintray_descriptor.json') as f:
		descriptor = json.load(f)		
		descriptor["version"]["name"] = version
		for f in descriptor["files"]:
			f["matrixParams"]["deb_distribution"] = dist
			f["matrixParams"]["deb_architecture"] = arch
		with open('bintray_descriptor_tmp.json', "w") as outfile:
			json.dump(descriptor, outfile)
	
def main(argv):
	version = None
	dist = None
	arch = None
	try:
		opts, args = getopt.getopt(argv,"v:d:a:",["version=","dist=", "arch="])
	except getopt.GetoptError as err:
		print (err)
		print ('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-v", "--version"):
			
			version = arg
		elif opt in ("-d", "--dist"):
			dist = arg
		elif opt in ("-a", "--arch"):
			arch = arg

	if version and dist and arch:
		saveDescriptor(version, dist, arch)
		

if __name__ == "__main__":
   main(sys.argv[1:])
