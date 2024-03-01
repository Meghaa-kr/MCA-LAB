echo "enter a number"
read num
r=`expr $num % 2`
if [ $r -eq 0 ]
then
echo "its an even number"
else
echo "its an odd number"
fi


