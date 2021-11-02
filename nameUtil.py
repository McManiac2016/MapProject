from PIL import Image, ImageOps, ImageColor, ImageFont, ImageDraw
def addText(srcImg,textAdd):
    img = Image.open(srcImg) #srcImg is the map with the added border
    draw = ImageDraw.Draw(img)

# Get font from working directory. Visit https://www.wfonts.com/search?kwd=pmingliu to download fonts
    font = ImageFont.truetype("D:\pyCharmProjects\mapProject\Couple1.ttf", 375)


# Add font: position, text, color, font
    draw.text((1900,6400),textAdd,(0,0,0), font=font)

# Save image
    img.save("HartaScrisa.png")