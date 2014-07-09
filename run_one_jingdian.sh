url=$1
urlid=`echo $url | awk -F"/" '{print $4}'`
DATAPATH=/search/zf/bh3_jingdian/data/$urlid
mkdir $DATAPATH
page=$DATAPATH/$urlid
#page=$DATAPATH/`python urlmd5.py $url`

##get first page
sh getReviews.sh $url $page
##get pagination url
python getPaginationUrls.py $page $url > $page.paginations
##get paginations page
file=$page.paginations
for url in `cat $file`
do
#page=$DATAPATH/`python urlmd5.py $url`
urlid=`echo $url | awk -F"/" '{print $4}'`
page=$DATAPATH/$urlid
sh getReviews.sh $url $page
done

