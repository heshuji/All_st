import hashlib
url='http://slide.news.sina.com.cn/slide_1_86058_507110.html'
a=hashlib.md5(url.encode('utf-8')).hexdigest()
print(a)

import re 
s='what are you doing $750,000, haushi wier3000'
print(re.findall('[\d,]+',s))
help(re)