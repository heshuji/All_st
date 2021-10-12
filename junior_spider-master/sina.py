import requests
url='http://slide.news.sina.com.cn/slide_1_86058_507110.html'
r=requests.get(url)
r.encoding='utf-8'
# f=open('sina.html','w+',encoding='utf-8')
# f.write(r.text)
# f.close()
# print(r.text)

filename=url[url.rfind('/')+1:]
# print(filename)
stat_pos=url.find('//')+2
end_pos=url.find('/',stat_pos)
domain=url[stat_pos:end_pos]
filename=domain+'_'+filename
f=open(filename,'w')
f.write(r.text)
f.close