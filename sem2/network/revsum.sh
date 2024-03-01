#!/bin/bash
echo "Enter a number"
read num
sums=0
while [ $num -gt 0 ]
do
    remainder=$(( num % 10 ))
    sums=$((sums+remainder))
    num=$(( num / 10 ))
done
echo $sums
