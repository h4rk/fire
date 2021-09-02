#fire - File rename utility v0.1
#author: Alessandro Sala(ale.sala.97@gmail.com)
import os
import argparse
from glob import iglob


def rename(old, new, path):

	if path:
		#folder = path+"/**/*"
		folder = path
	else:
		#folder = os.getcwd()+"/**/*"
		folder = os.getcwd()

	#filelist = [f for f in iglob(folder, recursive=True) if os.path.isfile(f)]
	filelist = os.listdir(folder)

	print(filelist)
	
	for filename in filelist:
		newName = filename.replace(old, new)
		os.rename(filename, newName)

	return "Done"

	
def main():
	parser = argparse.ArgumentParser(description="Replace substring in filenames")
	parser.add_argument('old', help='old substring that need replacing')
	parser.add_argument('new', help='new subtring that replaces the old one')
	parser.add_argument('-p', '--path', help="the directory path for files, if not present takes current working directory")
	args = parser.parse_args()

	print(rename(args.old, args.new, args.path))


if __name__ == "__main__":
	main()