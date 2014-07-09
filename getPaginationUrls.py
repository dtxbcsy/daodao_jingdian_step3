import os
import sys
import re

fi=open(sys.argv[1],"r")
text=fi.read(1024*1024)
fi.close()

val="null"
idx=text.find("class=\"guiArw sprite-pageNext")
if idx==-1 : sys.exit(0)
idx=text.rfind("</a>",0,idx)
val=text[:idx]
idx=val.rfind(">")
val=val[idx+1:]
cnt_pages=0
try:
	cnt_pages=int(val)
except:
	cnt_pages=0
if cnt_pages==0 : sys.exit(-1)

url=sys.argv[2]
idx=url.find("Reviews-")
url1=url[:idx+8]
url2=url[idx+8:]

for idx in range(1,cnt_pages):
	print url1+"or"+str(idx*15)+"-"+url2
