from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active
ws['A1'] = 'You should see three logos below'

# create an image
# img1 = Image('Tulips.jpg')
img2=Image("1.png")
# add to worksheet and anchor next to cells
ws.add_image(img2, "A3")
ws.add_image(img2, "C5")
#注意不能将相同图片对象添加到不同单元格中，程序只会在一个位置生成多个图片。
#本例中的多个图片对象，则可以分配给多个不同单元格对象

wb.save(u'f:\\示例.xlsx')