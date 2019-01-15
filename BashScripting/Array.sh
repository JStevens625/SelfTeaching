#!/bin/bash

for i in {1..4};
do
	N="NAME0"
	N="$N$i"
	array[i]=$N
done
echo "${array[@]}"
