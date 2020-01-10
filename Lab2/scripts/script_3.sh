#!/bin/bash
arr=( "$@" )
n=$#
p=$((n-1))
for ((i=0; i<$n; i++))
do
	for ((j=0; j<$p; j++))
	do
		if ((${arr[$j]} < ${arr[$((j+1))]}))
		then
			temp=${arr[$j]}
			arr[$j]=${arr[$((j+1))]}
			arr[$(($j+1))]=$temp
		fi
	done
done
for ((i=0; i<$n; i++))
do
	echo ${arr[$i]}
done
