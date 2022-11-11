#fire - File rename utility v0.2
#last_modified: 11-11-2022
#author: Alessandro Sala(ale.sala.97@gmail.com)
import os
import argparse
from glob import iglob


def rename(old, new, path):

	if path:
		folder = path
	else:
		folder = os.getcwd()

	filelist = os.listdir(folder)

	print(filelist)
	count=0
	for filename in filelist:
		if old in filename:
			newName = filename.replace(old, new)
			os.rename(folder+"/"+filename, folder+"/"+newName)
			count+=1

	return "Done. " + str(count) + " element(s) renamed."

	
def main():
	parser = argparse.ArgumentParser(description="Replace substring in filenames")
	parser.add_argument('old', help='old substring that need replacing')
	parser.add_argument('new', help='new subtring that replaces the old one')
	parser.add_argument('-p', '--path', help="the directory path for files, if not present takes current working directory")
	args = parser.parse_args()

	print(rename(args.old, args.new, args.path))


if __name__ == "__main__":
	main()
