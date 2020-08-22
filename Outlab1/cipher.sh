#!/bin/bash
if [ -n $1 ]
then
    touch encrypted.txt
	wget $1 > encrypted.txt
    chmod 775 letter.txt
    cp letter.txt encrypted.txt
	chmod 775 encrypted.txt
else
	echo "Usage: ./cipher.sh <url>"
    exit 1
fi
line=$(tail -1 encrypted.txt)

for I in $(seq 25); do
    echo $I $line | tr $(printf %${I}s | tr ' ' '.')\A-Z A-ZA-Z | tr $(printf %${I}s | tr ' ' '.')\a-z a-za-z > file.txt
    chmod 765 file.txt
    s1=$(grep -i Majesty file.txt)
    s2=$(grep -i Queen file.txt)
     if [ -n "$s1" ] || [ -n "$s2" ]
     then
         #dual=ABCDEFGHIJKLMNOPQRSTUVWXYZ
         #dual2=abcdefghijklmnopqrstuvwxyz
     	 rotat=$I
         touch  deciphered.txt
         input="encrypted.txt"
     	 while IFS= read -r l
         do
            echo $l | tr $(printf %${rotat}s | tr ' ' ';')\A-Z A-ZA-Z | tr $(printf %${rotat}s | tr ' ' ';')\a-z a-za-z >> deciphered.txt
         done < "$input"
            
         chmod 775 deciphered.txt
         let rotat=26-$I
         #dual=ABCDEFGHIJKLMNOPQRSTUVWXYZ
         #dual2=abcdefghijklmnopqrstuvwxyz
         #encripted_msg="PS. Give me the names"
		 #encripted_msg2=$(sed "y/${dual}/${dual:$rotat}${dual::$rotat}/" <<< $encripted_msg)
         #encripted_msg3=$(sed "y/${dual2}/${dual2:$rotat}${dual2::$rotat}/" <<< $encripted_msg2)
         #cat encripted.txt
		 #echo $encripted_msg3 | tee -a encripted.txt 
         echo PS. Give me the names | tr $(printf %${rotat}s | tr ' ' ';')\A-Z A-ZA-Z | tr $(printf %${rotat}s | tr ' ' ';')\a-z a-za-z >> encrypted.txt
         break
         #chmod 775 /bash/encripted.txt

     else
        continue
     fi
    

done
