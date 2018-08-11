import getUrl as t
from urllib import request
import re

filename = '../blogUrl.txt'

url_name = t.getUrl(filename)

html = request.urlopen(url_name).read()

view_pattern = re.compile(r'dd\stitle="[0-9]+')

rank_pattern = re.compile(r'dl\stitle="[0-9]+')

view_result = view_pattern.findall(str(html))
rank_result = rank_pattern.findall(str(html))


view_num = int(view_result[0].split("=\"")[1])
rank_num = int(rank_result[0].split("=\"")[1])
print("view_num=",view_num)
print("rank_view=",rank_num)



