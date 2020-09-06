# Enter your code here
import argparse
#MAXIMUM LEN OF INPUT ,,,IS THIS EFFICIENT ENOUGH??
#Parser for the command line flags
parser = argparse.ArgumentParser()
parser.add_argument("-ca","--candies",dest='candies')
parser.add_argument("-ch","--children",dest='children')

args=parser.parse_args()

with open(args.candies) as file_object:
	lines_candies = file_object.readlines()

M = int(lines_candies[0])

candy_types = lines_candies[1].split()
type_count = {}
for candy_type in candy_types:
	if candy_type in type_count:
		type_count[candy_type]+=1
	else:
		type_count[candy_type]=1	

with open(args.children) as file_object:
	lines_child = file_object.readlines()

N = int(lines_child[0])
demand_price = {}
for i in range(1,N+1):
	line = lines_child[i].split()
	if line[0] in demand_price:
		demand_price[line[0]].append(int(line[1]))
	else:
		demand_price[line[0]]=[int(line[1])]

for i in demand_price:
	demand_price[i].sort(reverse=True)


earned=0
for candy_type in demand_price:
	if candy_type in type_count:
		less = min(len(demand_price[candy_type]),type_count[candy_type])
		for m in range(0,less):
			earned+=demand_price[candy_type][m] 


print(earned)			