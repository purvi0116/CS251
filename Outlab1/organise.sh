mkdir playlists
mkdir albums
chmod 775 playlists
chmod 775 albums
for file in *
do
	if [ "$file" = "organise.sh" ]
	then
		continue
	fi
	#n=$(cat $file | head -2 | tail -1)
	#let b=3+$n-1
	#s=$(seq 3 $b | xargs -n 5 echo)
	alb=$(cat $file | head -1 | tail -1)
	n=$(cat $file | head -2 | tail -1)
	input="$file"
    while IFS= read -r l
        do
            if [ "$l" = "$alb" ]
			then
				cd albums
				mkdir -- "$alb"
				cd ..
				ln -s "../../$file" "./albums/$alb"
		
			elif [ "$l" = "$n" ]
			then
				continue
			else
				cd playlists
				mkdir -- "$l"
				cd ..
				ln -s "../../$file" "./playlists/$l"
			fi
         done < "$input"
		
	
done