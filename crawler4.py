import urllib.request
import http.cookiejar

# head: dict of header
def makeMyOpener(head = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makeMyOpener()
uop = oper.open('http://www.baidu.com/', timeout = 1000)
data = uop.read()
dat = data.decode()
print(dat)

def saveFile(data):
    save_path = '/Users/zhangyepei/Desktop/python_test/temp.out'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()

saveFile(data)
