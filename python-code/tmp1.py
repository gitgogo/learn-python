#coding=utf-8
from PIL import Image
def split_image(img, part_size=(64, 64)):
    # 将图片按给定大小切分
    w, h = img.size
    pw, ph = part_size
    assert w % pw == h % ph == 0
    return [img.crop((i, j, i + pw, j + ph)) 
    	for i in xrange(0, w, pw) for j in xrange(0, h, ph)]

img=Image.open('/Users/ralphliu/Desktop/1.png').resize((256,256))
h=split_image(img)
print h,len(h),img

# [<PIL.Image.Image image mode=RGBA size=64x64 at 0x103761440>
# [<PIL.Image._ImageCrop image mode=RGBA size=64x64 at 0x1092E3320>