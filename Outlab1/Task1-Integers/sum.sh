#! /bin/bash

count=($#)

if [ $count -eq 2 ]
then
	#let res=${numbers[0]}+${numbers[1]}
	let res=$1+$2
	#res2=$(( ${numbers[0]}+${numbers[1]} ))
	echo $res
	#echo "result using double parenthesis is: "$res2
	exit 0
else	
	echo "Wrong number of arguments, expected 2 got $count"
	exit 1
fi		


