import requests
r=requests.get('https://api.github.com/user',auth=('user','pass'))
print r.status_code,r.headers['content-type'],r.encoding,r.content,r.text,r.json()
r.encoding='utf-8'
