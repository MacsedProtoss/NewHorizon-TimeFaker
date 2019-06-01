import requests
import time

url="http://202.114.27.5/login/hponlinetime.php"

Cookies=input("输入你所获取到的Cookie：")

payload=[{'mesg': 'one'},{'mesg':'two'}]
headers={"Host":"202.114.27.5","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Linux; Android Q; Brand PhoneModel seriesNumber)","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Referer":"http://202.114.27.5/login/myhome.php","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7","Cookie":Cookies,"Connection":"keep-alive"}
s = requests.Session()
r = s.get(url, headers=headers)

print (r.status_code)


while True:
    time.sleep(1)
    r = s.get(url, headers=headers)
    print (r.status_code)

