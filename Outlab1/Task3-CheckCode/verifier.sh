#! /bin/bash
if [[ $# -ne 3 ]]
then
	echo "Usage: ./verifier.sh <source file> <testcases url> <cut-dirs arg>"
	exit 1
fi
rm -rf verifier feedback.txt failure.cpp a.out my_outputs
#-np to not download parent directory, -R to remove the index.html, inde.html.tmp files
wget  -np -r -nH -q --cut-dirs=$3 -R index.html* $2
cp $1 '.'
cppfile=`basename $1`
g++ $cppfile

directory_name=$2
base_dir=`basename $directory_name`
inp="$base_dir/inputs/"
out="$base_dir/outputs/"

mkdir $base_dir/my_outputs
for in_test in $(ls -I README.txt $inp)
do 
	n=${#in_test}
	n=$(( n-3 ))
	my_out=${in_test:0:$n}
	my_out=$my_out".out"
	./a.out < "$inp$in_test" > "$base_dir/my_outputs/$my_out"
done

touch feedback.txt
echo "Failed testcases are:">>'feedback.txt'

let num_failed=0
for out_test in $(ls -I README.txt $out)
do 
	d=`diff $out$out_test $base_dir/my_outputs/$out_test`
	if [[ ! $d = "" ]]
	then
		n=${#out_test}
		n=$(( n-4 ))
		fail=${out_test:0:$n}
		echo $fail>>'feedback.txt'
		(( num_failed++ ))
	fi	
			
done

if [[ $num_failed -eq 0 ]]
then
	echo "All testcases passed"
else
	echo "Some testcases failed"
fi		

exit 0