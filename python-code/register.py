#encoding=utf-8
import requests
import json

print "register------"
data = json.dumps({'username': 'Sasha', 'password': 'test1234', 'email': 'lily@qq.com'}) #
r = requests.post('http://103.36.173.17:8080/register/', data= data)
print r.status_code
print r.text
print type(r.json())
print str(r.json())
