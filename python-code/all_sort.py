#coding=utf-8
import random
"""
计算时间复杂度：
O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<...<O(n!)
冒泡排序：n^2/2-n/2-->O(n^2)
插入排序：最好情况：n-1-->O(n)；最坏情况：n^2/2-n/2-->O(n^2)
"""
#冒泡排序
def bubbl_sort(lisx):
	xlen=len(listx)
	for i in range(xlen-1):
		for j in range(xlen-1-i):
			if listx[j]>listx[j+1]:
				listx[j],listx[j+1]=listx[j+1],listx[j]
	return listx

#插入排序
def insert_sort(listx):
	xlen=len(listx)
	for i in range(1,xlen):
		key=listx[i]
		j=i-1
		while j>=0:
			if listx[j]>key:
				listx[j],listx[j+1]=listx[j+1],listx[j]
				j-=1
			else:
				break
	return listx

#选择排序
def select_sort(listx):
	xlen=len(listx)
	for i in range(xlen):
		min=i 
		for j in range(i+1,xlen):
			if listx[min]>listx[j]:
				min=j
		listx[i],listx[min]=listx[min],listx[i]
	return listx

#快速排序
def quickSort(listx):
	xlen=len(listx)
	def pathSort(lista,sIndex,eIndex):
		# flag=lista[eIndex]
		i=sIndex-1
		for j in range(sIndex,eIndex):
			if lista[j]>lista[eIndex]:
				pass
			else:
				i+=1
				lista[j],lista[i]=lista[i],lista[j]
		lista[i+1],lista[eIndex]=lista[eIndex],lista[i+1]
		return i+1
	def qsort(listb,sIndex,eIndex):
		if sIndex>=eIndex:
			return listb
		middle=pathSort(listb,sIndex,eIndex)
		qsort(listb,sIndex,middle-1)
		qsort(listb,middle+1,eIndex)
		return listb
	qsort(listx,0,len(listx)-1)
	return listx

if __name__ == '__main__':
	listx=range(1,15)
	random.shuffle(listx)
	print listx
	# print insert_sort(listx)
	# print bubbl_sort(listx)
	print select_sort(listx)