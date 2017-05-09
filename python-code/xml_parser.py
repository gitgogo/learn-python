#coding=utf-8
# from xml.dom.minidom import parse
# import xml.dom.minidom
# # 使用minidom解析器打开 XML 文档
# DOMTree = xml.dom.minidom.parse(r"movies.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("shelf"):
#    print "Root element : %s" % collection.getAttribute("shelf")
# # 在集合中获取所有电影
# movies = collection.getElementsByTagName("movie")
# # 打印每部电影的详细信息
# for movie in movies:
#    print "*****Movie*****"
#    if movie.hasAttribute("title"):
#       print "Title: %s" % movie.getAttribute("title")
#    type = movie.getElementsByTagName('type')[0]
#    print "Type: %s" % type.childNodes[0].data
#    format = movie.getElementsByTagName('format')[0]
#    print "Format: %s" % format.childNodes[0].data
#    rating = movie.getElementsByTagName('rating')[0]
#    print "Rating: %s" % rating.childNodes[0].data
#    description = movie.getElementsByTagName('description')[0]
#    print "Description: %s" % description.childNodes[0].data

# import xml.dom.minidom
# #在内存中创建一个空的文档
# doc = xml.dom.minidom.Document()
# print doc
# #创建一个根节点Managers对象
# root = doc.createElement('Managers')
# print u"添加的xml标签为：", root.tagName
# # 给根节点root添加属性
# root.setAttribute('company', 'xx科技')
# value = root.getAttribute('company')
# print u"root元素的'company'属性值为：", value
# root.setAttribute('name', '光荣之路教育科技有限公司')
# # 给根节点添加一个叶子节点
# ceo = doc.createElement('CEO')
# #给叶子节点name设置一个文本节点，用于显示文本内容
# ceo.appendChild(doc.createTextNode('吴总'))
# print ceo.tagName
# print u"给叶子节点添加文本节点成功"
# print ceo.toxml(),'\n',root.toxml()

#coding=utf-8
import xml.dom.minidom
import codecs
#在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
#创建一个根节点company对象
root = doc.createElement('companys')
# 给根节点root添加属性
root.setAttribute('name', u'公司信息')
#将根节点添加到文档对象中
doc.appendChild(root) 

# 给根节点添加一个叶子节点
company = doc.createElement('gloryroad')
# 叶子节点下再嵌套叶子节点
name = doc.createElement("Name")
# 给节点添加文本节点
name.appendChild(doc.createTextNode(u"光荣之路教育科技公司"))

ceo = doc.createElement('CEO')
ceo.appendChild(doc.createTextNode(u'吴总'))
# 将各叶子节点添加到父节点company中
# 然后将company添加到跟节点companys中
company.appendChild(name)
company.appendChild(ceo)
root.appendChild(company)
# print doc.toxml()
fp = codecs.open('company.xml', 'w','utf-8')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding="utf-8")
fp.close()

#coding=utf-8
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='movies.xml')
root=tree.getroot()
print root.tag
print root.attrib

for child_of_root in root:
    print child_of_root.tag
    print "********", child_of_root.attrib

print "*"*50
print root[0].tag
print root[0].text
print root[0][0].tag
print root[0][0].text
print "*"*50

for elem in tree.iter():  #遍历所有元素，所有标签
    print elem.tag, elem.attrib
   
print "*"*50
for elem in tree.iterfind('movie/type'):#查找movie下的所有type标签
    print elem.tag, elem.attrib

for i in tree.findall("movie"):
    print "movie:",i,i.tag,i[0].tag,i[0].text
   
for i in tree.findall("movie/format"):
    print "movie:",i,i.tag,i.tag,i.text

   
print "*"*50
for elem in tree.iter('tag=stars'):#查找标签为star的元素
    print elem.tag, elem.attrib
print "*"*50
for elem in tree.iterfind('*[@title="Ishtar"]'): #查找属性为title="Ishtar"的元素
    print elem.tag, elem.attrib

print "-"*50
root = tree.getroot()                #获取<collection>元素
print "root:",root[0].tag            #打印第一级movie元素的标签，为movie
print "subnode:",root[0][0].tag      #打印第一级movie元素下的第一个子元素标签type
print "subnode:",root[0][1].tag      #打印第一级movie元素下的第二个子元素标签format
print "subnode:",root[0][2].tag      #打印第一级movie元素下的第三个子元素标签year
print "subnode:",root[0][3].tag      #打印第一级movie元素下的第四个子元素标签rating

print "subnode:",root[0][4].tag      #打印第一级movie元素下的第五个子元素标签stars
del root[0][4] #删除第一级movie元素下的第四个子元素
del root[0][3] #删除第一级movie元素下的第三个子元素
del root[0][2] #删除第一级movie元素下的第二个子元素
del root[0][1] #删除第一级movie元素下的第一个子元素

del root[3] #删除第四个movie元素
del root[2] #删除第三个movie元素
for subelem in root:
    print subelem.tag, subelem.attrib  #打印第一个movie和第二个movie元素的标签和属性

tree.write(sys.stdout)  #将xml文件的内容写到屏幕上
#tree.write("d:\\movies.xml")  #将变更的xml文件写入到文件中