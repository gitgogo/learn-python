#coding=utf-8
# s='adalhlskafahkfhahfkshfksfhwfewfwfs'
l=[2,3,6,7,4,1,9]
for i in range(1,len(l)/2+1):
	l.remove(l[i])

print l #[2, 6, 4, 9]