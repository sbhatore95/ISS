#!/bin/bash
arr=($(ls))
n=${#arr[@]}
for ((i=0;i<$n;i++))
do
	mv ${arr[$i]} "${arr[$i]}.tar"
done
