#coding=utf-8
class HotelRoomCalc(object):
	'Hotel room rate calculator'
	def __init__(self,rt,sales=0.085,rm=0.1):
		'''HotelRoomCalc default arguments'''
		self.salesTax=sales
		self.roomTax=rm
		self.roomRate=rt

	def calcTotal(self,days=1):
		daliy=round(self.roomRate*(1+self.salesTax+self.roomTax),2)
		return float(days)*daliy

sfo=HotelRoomCalc(299)
sfo.calcTotal()
sfo.calcTotal(2)

sea=HotelRoomCalc(169,0.045,0.02)
sea.calcTotal(4)