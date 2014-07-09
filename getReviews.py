import os
import sys
import re

trim_pat_1=re.compile(r'[\n\r\t]',re.S|re.M)
trim_pat_2=re.compile(r'>[ ]*?<',re.S|re.M)

recommend_pat_1=re.compile(r'<img class="sprite-ratings" src="(.*?)></span><span class="(.*?)>(.*?)</span></div><div class="rating-list simple-rating">(.*?)</div>',re.S|re.M)
#recommend_pat_1=re.compile(r'<img class="sprite-ratings" src="(.*?)" alt="(.*?)" content="(.*?)"></span><span class="(.*?)>(.*?)</span></div><div class="rating-list simple-rating">(.*?)</div>',re.S|re.M)
#<ul class="recommend recommend-column"><li class="recommend-answer">性价比<b>(.*?)</b></li><li class="recommend-answer">舒适度<b>(.*?)</b></li><li class="recommend-answer">位置<b>(.*?)</b></li><li class="recommend-answer">卫生<b>(.*?)</b></li><li class="recommend-answer">服务<b>(.*?)</b></li><li class="recommend-answer">睡眠质量<b>(.*?)</b></li></ul></div>',re.S|re.M)
recommend_pat_2=re.compile(r'<div class="entry">(.*?)</div>',re.S|re.M)

recommend_pat_0=re.compile(r'<div id="expanded_review_(.*?)">(.*?)<div class="note">此点评仅代表旅行者个人的主观意见',re.S|re.M)

fi=open(sys.argv[1],"r")
text=fi.read(1024*1024)
fi.close()
text=trim_pat_1.sub('',text)
text=trim_pat_2.sub('><',text)

recommend_ret_0=recommend_pat_0.findall(text)

id=sys.argv[2]

for val in recommend_ret_0:
	recommend_ret_1=recommend_pat_1.findall(val[1])
	recommend_ret_2=recommend_pat_2.findall(val[1])
	if len(recommend_ret_1)==0 or len(recommend_ret_2)==0 : 
		print "[error]\t"+id+"\t"+val[1]
	else :print id+"\t"+"\t".join(recommend_ret_1[0])+"\t"+recommend_ret_2[0]

