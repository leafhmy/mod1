#一个网页_写入txt文件
import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
#url=""
try:
    data=urllib.request.urlopen(url).read().decode()
    #pat=''
    result=re.compile(pat).findall(data)
    #fh = open("", "")
    for i in range(len(result)):
        fh.write(result[i]+"\n")
    fh.close()
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
except Exception as e:
    print(e)
