#!/bin/bash

#While Loop
echo While Loop
i=0
while [ $i -le 10 ]
do
    ((i+=1))
    echo $i
done

#For Loop
echo For Loop
j=0
for j in {0..10..2}
do
    echo $j
done

#Until Loop
echo Until Loop
k=0
until [ $k -ge 10 ]
do
    ((k+=3))
    echo $k
done