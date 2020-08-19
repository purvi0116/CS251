#! /bin/bash
function romanValue {
	if [ $1 -eq 1 ]
	then	
		n='I'
	elif [ $1 -lt 4 ]
	then 
		let a=$1-1
		n+='I'$(./roman.sh $a)
	elif [ $1 -eq 4 ]
	then 
		n='IV'	
	elif [ $1 -eq 5 ]
	then
		n='V'	
	elif [ $1 -lt 9 ]
	then
		let a=$1-5
		n+='V'$(./roman.sh $a)		
	elif [ $1 -eq 9 ]
	then
		n='IX'	
	elif [ $1 -eq 10 ]
	then
		n='X'			
	
	
	elif [ $1 -le 39 ]
	then
		let a=$1-10
		n+='X'$(./roman.sh $a)
	elif [ $1 -eq 40 ]
	then
		n='XL'		
	elif [ $1 -le 49 ]
	then
		let a=$1-40
		n+='XL'$(./roman.sh $a)		
	elif [ $1 -eq 50 ]
	then
		n='L'			
	elif [ $1 -lt 90 ]
	then
		let a=$1-50
		n+='L'$(./roman.sh $a)
	elif [ $1 -eq 90 ]
	then
		n='XC'		
	elif [ $1 -le 99 ]
	then
		let a=$1-90
		n+='XC'$(./roman.sh $a)		
	elif [ $1 -eq 100 ]
	then
		n='C'	
	elif [ $1 -gt 100 ]
	then
		let a=$1-100
		n+='C'$(./roman.sh $a)		
	fi	
}
n=''
romanValue $1
echo $n