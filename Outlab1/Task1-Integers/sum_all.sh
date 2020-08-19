#! /bin/bash

num_arg=($#)
arr_num=($@)
#echo "arr is " $(./sum.sh 1 5)
let sum=0
	
if [ $num_arg -eq 0 ]
then 
	echo "No numbers given"
	exit 1
else	
	for (( i=0; i<$num_arg; i++))
	do 
		sum=$(./sum.sh ${arr_num[$i]} $sum)  
	done	
	echo "$sum"
	exit 0
fi	
