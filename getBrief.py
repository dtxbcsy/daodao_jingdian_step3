import os
import sys
import re

trim_pat_1=re.compile(r'[\n\r\t]',re.S|re.M)
trim_pat_2=re.compile(r'>[ ]*?<',re.S|re.M)

pat1=re.compile(r'<h1 id="HEADING" property="v:name">(.*?)</h1>',re.S|re.M)
pat2=re.compile(r'<img class="sprite-ratings-ltgrn" src="(.*?)" alt="(.*?)" content="(.*?)" title="(.*?)">',re.S|re.M)
pat3=re.compile(r'<span class="altHead">(.*?)</span>',re.S|re.M)
pat4=re.compile(r'<address>(.*?)</address>',re.S|re.M)


fi=open(sys.argv[1],"r")
text=fi.read(1024*1024)
fi.close()
text=trim_pat_1.sub('',text)
text=trim_pat_2.sub('><',text)

recommend_ret_0=recommend_pat_0.findall(text)

for val in recommend_ret_0:
	recommend_ret_1=recommend_pat_1.findall(val[1])
	recommend_ret_2=recommend_pat_2.findall(val[1])
	print "\t".join(recommend_ret_1[0])+"\t"+recommend_ret_2[0]

