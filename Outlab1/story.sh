#!/bin/bash
key=$2
touch "$3"
truncate -s 0 "./$3"
while [ 1 = 1 ]
do
for file in *; do
	
	if [ "$file" = "output.txt" ]
	then
		echo $file
		continue
	fi
	flag=0
    s=$(cat $file | head -2 | tail -1)
    if [ "$key" = "$s" ]
    then
    	let flag=1
    	line=$(cat $file | head -1 | tail -1)
		echo $line >> $3 
		key=$(cat $file | head -3 | tail -1)
		break
	fi

done
if [ $flag = 0 ]
	then
		break
	fi

done
