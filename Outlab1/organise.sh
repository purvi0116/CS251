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
	alb=$(sed "1q;d" "$file")
	n=$(sed "2q;d" "$file")
	sed -n '1,$ p' "$file" | while read line
	do
		
		if [ "$line" = "$alb" ]
		then
			cd albums
			mkdir -- "$alb"
			cd ..
			ln -s "../../$file" "./albums/$alb"
		
		elif [ "$line" = "$n" ]
		then
			continue
		else
			cd playlists
			mkdir -- "$line"
			cd ..
			ln -s "../../$file" "./playlists/$line"
		fi
	done
	#alb=$(sed "1q;d" "$file")
	#cd albums
	#mkdir -- "$alb"
	#cd ..
	##echo ......
	#echo $alb
	#echo ......
	#ln -s "../../$file" "./albums/$alb"
	
done