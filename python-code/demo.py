import urllib,urllib2
import base64
url=r'http://www.baidu.com/'
req = urllib2.Request(url)
base64string = base64.encode("18810936553:bd.441026")
authheader = "Basic "+base64string
req.add_header('Authori',authheader)
urllib2.urlopen(req)