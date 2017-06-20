#encoding=utf-8
from xml.etree import ElementTree

class ParseXML(object):
    def __init__(self, xmlPath):
        self.xmlPath = xmlPath

    def getRoot(self):
        # 打开将要解析的xml文件
        tree = ElementTree.parse(self.xmlPath)
        # 获取xml文件的根节点对象，也就是树的根
        # 然后返回给调用者
        return tree.getroot()

    def findNodeByName(self, parentNode, nodeName):
        # 通过节点的名字，获取节点对象
        nodes = parentNode.findall(nodeName)
        return nodes

    def getNodeOfChildText(self, node):
        # 获取节点node下所有子节点的节点名作为key，
        # 文本节点作为value组成的字典对象，若从0开始，则包含父节点的标签，例如book
        childrenTextDict = {i.tag: i.text for i in list(node.iter())[1:]}
        # print childrenTextDict
        # 上面代码等价于下面代码
        '''
        childrenTextDict = {}
        for i in list(node.iter())[1:]:
            childrenTextDict[i.tag] = i.text
        '''
        return childrenTextDict

    def getDataFromXml(self):
        # 获取xml文档树的根节点对象
        root = self.getRoot()
        # 获取根节点下所有名叫book的节点对象
        books = self.findNodeByName(root, "book")
        dataList = []
        # 遍历获取到的所有book节点对象，# 取得需要的测试数据
        for book in books:
            childrenText = self.getNodeOfChildText(book)
            dataList.append(childrenText)
            # print dataList
        return dataList

if __name__ == '__main__':
    xml = ParseXML(r"TestData.xml")
    datas = xml.getDataFromXml()
    for i in datas:
        print i["name"], i["author"]