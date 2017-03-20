#coding=utf-8
def structure_headers(self):
    form_data=urllib.urlencode({
        'email':self.user_name,
        'password':self.password,
        'webrequest':'true'
        })
    user_agent=('Mazilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)'
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/38.0.2125.111 Safari/537.36")
    XCSRF2Cookie='csrf2_token_%s'%''.join(self.random_string(8))
    XCSR2Token=''.join(self.random_string(24))
    XCSRFToken=''.join(self.random_string(24))
    cookie='csrftoken=%s; %s=%s'%(XCSRToken,XCSRF2Cookie,XCSR2Token)

    request_header={
    'Referer':'https://www.baidu.com',
    'User-Agent':user_agent,
    'X-Requested-With':'XMLHttpRequest',
    'X-CSRF2-Cookie':XCSRF2Cookie,
    'X-CSRFToken':XCSRFToken,
    'Cookie':cookie
    }
    return form_data,request_header