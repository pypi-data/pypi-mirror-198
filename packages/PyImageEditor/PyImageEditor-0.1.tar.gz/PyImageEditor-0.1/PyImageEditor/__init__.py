#
# PIE - Python Image Editor
#

from PIL import Image, ImageDraw, ImageFont
def createImg(w=100, h=100, color="#000"):
  return Image.new(mode="RGB", size=(w, h), color=color)
def openImg(imgurl):
  return Image.open(imgurl)
def writeText(img, text, fontID="Arial.ttf", fontSize=32, color="#000", x=0, y=0, centerAlign=False):
  lines = text.split("\n")
  if len(lines) > 1:
    for i in range(len(lines)):
      img = writeText(img, lines[i], fontID=fontID, fontSize=fontSize, color=color, x=x, y=y+fontSize*i, centerAlign=centerAlign)
    return img
  font = ImageFont.truetype('C:\Windows\Fonts\\'+fontID, fontSize)
  if centerAlign:
    x = x + round((img.width - font.getlength(text))/2)
  draw = ImageDraw.Draw(img)
  draw.text((x, y),text,font=font,fill=color)
  return img
def overlayimage(img1, img2, x=0, y=0):
  img1.paste(img2, (x,y), img2)
  return img1
def drawCircle(img, shape=[0, 0, 50, 50], color="#000"):
  draw = ImageDraw.Draw(img)
  draw.ellipse(shape, fill=color)
  return img
def drawRectangle(img, shape=[0, 0, 50, 50], color="#000"):
  draw = ImageDraw.Draw(img)
  draw.rectangle(shape, fill=color)
  return img
def drawLine(img, xy1=(0,0), xy2=(100,100), color="#000", width=2):
  draw = ImageDraw.Draw(img)
  draw.line([xy1, xy2], fill=color,width=width)
  return img