import getUrl
from urllib import request
import re
import time
import os

targetFile = 'viewAndRank.txt'


if os.path.exists(targetFile):
	pass
	print(targetFile, ' is existed')
else:
	with open(targetFile, 'w') as t:
		t.write('date\t\t\tViewNum\t\tRankNum\n') 
		t.close()

now = time.strftime('%Y-%m-%d %H:%M:%S')


filename = '../blogUrl.txt'

url_name = getUrl.getUrl(filename)

html = request.urlopen(url_name).read()

view_pattern = re.compile(r'dd\stitle="[0-9]+')

rank_pattern = re.compile(r'dl\stitle="[0-9]+')

view_result = view_pattern.findall(str(html))
rank_result = rank_pattern.findall(str(html))


view_num = view_result[0].split("=\"")[1]
rank_num = rank_result[0].split("=\"")[1]
print("view_num=",view_num)
print("rank_view=",rank_num)


with open('viewAndRank.txt', 'a') as t:
	info = now + '\t' + view_num + '\t\t'+ rank_num + '\n'
	t.write(info)
	t.close()

