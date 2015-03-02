

import sys
import re
import os
import utils

def main():
	files = utils.troll_directories(os.path.normpath(sys.argv[1]))
	patterns = utils.convert_patterns(sys.argv[2:])
	utils.apply_patterns(files, patterns)


if __name__ == '__main__' : main()


