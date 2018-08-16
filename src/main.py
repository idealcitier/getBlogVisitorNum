import getUrl
import getInfo
from urllib import request
import re
import time
import os

targetFile = './viewAndRank.txt'
url_filename = './blogUrl.txt'

if os.path.exists(targetFile):
	print(targetFile, ' is existed')
else:
	print('creat ', targetFile , " to store CSDN blog's  view and rank num")
	with open(targetFile, 'w') as t:
		t.write('date\t\t\tViewNum\t\tRankNum\n') 
		t.close()

now = time.strftime('%Y-%m-%d %H:%M:%S')

view_num, rank_num = getInfo.getInfo(url_filename)

with open(targetFile, 'a') as t:
	info = now + '\t' + view_num + '\t\t'+ rank_num + '\n'
	t.write(info)
	t.close()

