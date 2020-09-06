# Enter your code here
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-inp', action="store", dest="inp")
parser.add_argument('-out', action="store", dest="out")
args = parser.parse_args()

inp = open(args.inp, 'r')

out = open(args.out, 'w')
for l in inp:
	canonical_path = os.path.normpath(l.strip('\n'))
	if canonical_path == ' ' or canonical_path == '.':
		canonical_path = '/'
	out.write(canonical_path)