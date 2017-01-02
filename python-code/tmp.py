#coding=utf-8
import string
def raise_exception():
	num=raw_input('input a number->')
	if num not in string.digits:
		raise TypeError('must be number!')
def hadle():
	try:
		raise_exception()
	except TypeError,e:
		print e

hadle()