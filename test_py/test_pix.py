#!/usr/bin/python

from PIL import Image

im = Image.open("/home/xwang/test/test_img/captcha.gif")
im.convert("P")

im2 = Image.new("P", im.size, 255)

for x in range(im.size[1]):
  for y in range(im.size[0]):
    pix = im.getpixel((y, x))

    if pix == 220:
      im2.putpixel((y, x), 0)

im2.save("/home/xwang/test/test_img/output2.gif")


