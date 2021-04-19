import os
import sys,getopt
import shutil
import time
from calcolate_zI import *
from merger import *

# short_options = "g:z:"
# long_options = ["group=","zi="]
# argument_list = sys.argv[1:]
#
# max_dimension = 3
# max_zI = 3
#
# try:
#     arguments, values = getopt.getopt(argument_list, short_options, long_options)
# except getopt.error as err:
#     # Output error, and return with an error code
#     print (str(err))
#     sys.exit(2)
#
# for current_argument, current_value in arguments:
#     if current_argument in ("-g", "--group"):
#         max_dimension = int(current_value)
#     elif current_argument in ("-z", "--zi"):
#         max_zI = float(current_value)
#     else:
#         print("missing argoument, take a look at the ReadMe for more information")
#         sys.exit(2)
#
# print(max_dimension)
# print(max_zI)

def run_zi(max_dimension,max_zI):
	all_file = os.listdir("files")
	for file in all_file:
		if (shutil.copy("files/{0}".format(file), "file.txt")):
			if os.path.exists("results") and os.path.isdir("results"):
				shutil.rmtree("results")
			os.system("mkdir results")
			open("sequence.txt", 'a').close()
			num = 0
			exit = 0
			while(exit <= 1):
				num+=1
				os.system("mkdir {}".format(num))
				calcolate_zi(max_dimension)
				#os.system("python3 calcolate_zI.py {}".format(max_dimension))
				shutil.copy("file.txt", "{}/".format(num))
				print(exit)
				exit = merge(max_zI)
				#exit = os.system("python3 merger.py {}".format(max_zI))
				shutil.move("grind.txt", "{}/".format(num))
				shutil.move("{}/".format(num), "results")
				print("-----------------")

			if os.path.exists(file) and os.path.isdir(file):
				shutil.rmtree(file)
			os.system("mkdir {}".format(file))
			os.remove("file.txt")
			shutil.move("results", "{}/".format(file))
			shutil.move("sequence.txt", "{}/".format(file))
