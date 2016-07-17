 # from http://www.yiibai.com/python/python3-webbug-series1.html

import gzip
import re
import http.cookiejar
import urllib.parse

def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch'
}

url = 'http://www.zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)     # 解压
_xsrf = getXSRF(data.decode())

url += '#signin'
id = 'XXXX'
password = 'XXX'
postDict = {
        '_xsrf':_xsrf,
        'account': id,
        'password': password,
        'remember_me': 'true'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode())
