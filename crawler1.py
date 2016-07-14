#encoding:UTF-8
import urllib.request
def getdata():
    url="http://www.baidu.com"
    data=urllib.request.urlopen(url).read()
    z_data=data.decode('UTF-8')
    print(z_data)

getdata()
