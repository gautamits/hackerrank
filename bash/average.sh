read a
i=0
sum=0
while [ $i -lt $a ]
do
    read j
    sum=$(( sum + j ))
    i=$(( i + 1 ))
done
printf %.3f $(echo "scale = 4; $sum/$a" | bc -l)
echo ""
