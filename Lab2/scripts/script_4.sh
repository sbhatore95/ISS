#!/bin/bash
arr=($(ls))
n=${#arr[@]}
for ((i=0;i<$n;i++))
do
	if [ ${arr[$i]} != "script_4.sh" ]
	then
		mv ${arr[$i]} "${arr[$i]}.try"
	fi
done
