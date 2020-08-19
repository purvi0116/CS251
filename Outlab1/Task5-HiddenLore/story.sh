#! /bin/bash

#why in hints exit status is written
directory=$1
start_key=$2
output=$3
finish=0
count=0
key=$start_key
found=0
a=`ls $directory` 
for file in `ls $directory`
	do
		key_this=`cut -d$'\n' -f 2 $directory/$file`
		(( count++ ))
		if [[ $key -eq $key_this ]]
		then
			key=`cut -d$'\n' -f 3 $directory/$file`  #cut the file using delimiter asa newline 
			echo `cut -d$'\n' -f 1 "$directory/$file"  > "$output" `  #overwrite in beginning
			break	
		fi	
		
done

while [ $finish = 0 ]
do
	for file in `ls $directory`
	do
		found=0
		key_this=`cut -d$'\n' -f 2 $directory/$file`
		(( count++ ))
		if [[ $key -eq $key_this ]]
		then
			key=`cut -d$'\n' -f 3 $directory/$file`
			echo `cut -d$'\n' -f 1 "$directory/$file" ` >> "$output"
			found=1
			break	
		fi	
		
	done
	if [[ $found -eq 0 ]]
	then	
		finish=1
	fi	
done		
	#cut -d$'\n' -f 2 $directory/10.txt 
echo $count


echo $a
#PATTERN="12.txt"
#VAR="0.txt 1.txt 4.txt 10.txt 12.txt 13.txt"
#printf -v NEW_VAR '%s' "${VAR##*$PATTERN}"
#echo "$NEW_VAR"


#if grep taken o(n) then o(n2) else o(n)

#max around 100 files 