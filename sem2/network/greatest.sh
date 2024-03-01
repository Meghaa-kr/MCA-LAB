echo "Enter number1"
read a 
echo "enter number2"
read b
echo "enter number3"
read c
if [ $a -gt $b ] && [ $a -gt $c ]
then
echo "$a is Greatest"
elif [ $b -gt $c ] && [$b -gt $a ]
then
echo "$b is Greatest"
else
echo "$c is Greatest!"
fi
