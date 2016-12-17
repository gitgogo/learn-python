#coding=utf-8
fp = open(r'f:\1.txt')
aList = []
for item in fp:
    if item.strip():
        aList.append(item)
fp.close()
fp = open(r'f:\4.txt','w')
fp.writelines(aList)
fp.close()
