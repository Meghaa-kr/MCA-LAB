#!/bin/bash
echo "please enter first number"
read a
echo "please enter second number"
read b
echo "please enter third number"
read c
echo "please enter 4th number"
read d
s=$(($a+$b+$c+$d))
echo "sum" $s
p=$(($a*$b*$c*$d))
echo "product"$p
avg=$(($s/4))
echo "average" $avg
