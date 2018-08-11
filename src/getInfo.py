import getUrl as t
from urllib import request
import re


def getInfo(filename):
	
	url_name = t.getUrl(filename)

	html = request.urlopen(url_name).read()

	view_pattern = re.compile(r'dd\stitle="[0-9]+')

	rank_pattern = re.compile(r'dl\stitle="[0-9]+')

	view_result = view_pattern.findall(str(html))
	rank_result = rank_pattern.findall(str(html))


	view_num = view_result[0].split("=\"")[1]
	rank_num = rank_result[0].split("=\"")[1]
#	print("view_num=",view_num)
#	print("rank_view=",rank_num)
	return view_num, rank_num



#filename = '../blogUrl.txt'
#getInfo(filename)
