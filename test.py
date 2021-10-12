import requests

url = 'http://211.68.250.78:8080/eams/loginExt.action'
fout = open('result.txt', 'w')
for i in range(1):
    r=requests.get(url)
    fout.write(str(i+1)+' ： OK with status_code: '+str(r.text)+'\n')
    print(str(i+1)+' ： OK with status_code: '+str(r.text)+'\n')
fout.close()

