#!/bin/bash
if [ $# -ne 2 ]
then
echo “Command line arguments missing”
exit
fi
echo `expr $1 + $2`
echo $(($1+$2))
