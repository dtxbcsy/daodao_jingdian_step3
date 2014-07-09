mkdir data

declare -i count=0

for url in `cat input`
do
sh run_one_jingdian.sh $url & 
((count=($count+1)%50))
if [ $count -eq 0 ]
then
wait
fi
done

wait
