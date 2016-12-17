#encoding=utf-8
import socket
t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

t.connect(('smtp.126.com', 25))
print "start", t.recv(1024)
t.send("helo 126.com\r\n")

print "111", t.recv(1024)
t.send("auth login\r\n")
print "222", t.recv(1024)
t.send("dGVzdG1hbjE5ODA=\r\n")
print "333", t.recv(1024)
t.send("Zm9zdGVyd3UxOTc4\r\n")
print "444", t.recv(1024)
t.send("mail from:<testman1980@126.com>\r\n")
print "555", t.recv(1024)
t.send("rcpt to:<865479851@qqcom>\r\n")
print "666", t.recv(1024)
t.send("data\r\n")
print "777", t.recv(1024)

#发送邮件内容
t.send("from:testman1980@126.com\r\n")  #optional，可伪造别人的发件记录
t.send("to:ldjwyyx@163.com\r\n")   #optional,可发给任何人
t.send("subject:shut up!!!\r\n")
t.send("\r\n")  #按照smtp协议要求，在标题后要发个空行
t.send("wow!\r\n")
t.send(".\r\n")
print "888", t.recv(1024)
