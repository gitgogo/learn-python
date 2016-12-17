import urllib,urllib2
import base64
url=r'https://www.baidu.com/'
base64string = base64.encodestring('18810936553:baidu.441026').strip()
authheader="Basic "+base64string
req=urllib2.Request(url)
req.add_header('Authorization',authheader)
html=urllib2.urlopen(req)
print html.info(),req.get_header('Authorization'),req.get_full_url()
