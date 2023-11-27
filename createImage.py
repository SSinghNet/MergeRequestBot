import cv2
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def createImage(messageText):
    img = Image.open("template.jpg")
    draw = ImageDraw.Draw(img)

    width, height = img.size 
    font = ImageFont.truetype("POE Sans Pro Light.ttf", 75)

    textwidth, textheight = draw.textsize(messageText, font=font)
    x = width/2 - textwidth/2
    y = height/9 - textheight/9
    
    draw.text((x, y), messageText, (0,0,0),font=font)

    img.save("output.jpg")

createImage("MERGE REQUEST?????")