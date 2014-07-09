url=$1
page=$2
proxy_path=/search/zf/proxy

for((t=0;t<10;t++))
do
	sh /search/zf/proxy/wget.sh $url $page
	##get more reviews
	target=`fgrep "<div id=\"review_" $page | awk -F"_" '{print $2}' | awk -F"\"" 'NR==1{printf $1}'`
	reviews=`fgrep "<div id=\"review_" $page | awk -F"_" '{print $2}' | awk -F"\"" '{printf $1","}'`
	midfix=`echo $url | awk -F"Attraction_Review-" '{print $2}' | awk -F"Reviews" '{printf $1}'`

	if [ -s $page ] && [ "$target"x != ""x ]
	then
		echo "***succ:" 1>&2
		break
	fi
	echo "failed page" 1>&2
done

page=$page.more

for((t=0;t<10;t++))
do
	url="http://www.daodao.com/ExpandedUserReviews-$midfix?target=$target&context=1&reviews=$reviews&servlet=Attraction_Review&expand=1&extraad=true&extraadtarget=1"
	sh /search/zf/proxy/wget.sh $url $page
	ret_3=`grep "404 Not Found" $page.log | wc -l | awk '{printf $1}'`
	if [ $ret_3 != "0" ]
	then
		echo "failed page mor 404" 1>&2
		touch $page.output
		break
	fi

	python getReviews.py $page $url > $page.output 

	if [ -s $page.output ]
	then
		echo "***succ:" 1>&2
		break
	fi
	echo "failed page more" 1>&2
done
