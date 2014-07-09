import hashlib
import os
import sys

def get_md5_value(src):	
	myMd5 = hashlib.md5()
	myMd5.update(src)
	myMd5_Digest = myMd5.hexdigest()
	return myMd5_Digest

sys.stdout.write(get_md5_value(sys.argv[1]))
