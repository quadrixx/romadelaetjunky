from PIL import Image, ImageFont, ImageDraw
import math

filename = "pics/шаман.jpg"
dem_empty = "black.png"
with Image.open(filename) as img:
    img.load()
    with Image.open(dem_empty) as dem:
        dem.load()
        size = img.size
        width = size[0] + 110
        height = size[1] + 160
        dem = dem.crop((0, 0, width, height))
        draw = ImageDraw.Draw(dem)
        pic_x = round(width/2-size[0]/2)
        pic_y = round(height/2-size[1]/2-height/10)
        dem.paste(img, (pic_x,pic_y))
        upper_font = ImageFont.truetype("times.ttf", size = round(height/10))
        upper_text = "ДЕМОТИВАТОР МНОГО ТЕКСТА МНОГО ТЕКСТА МНОГО ТЕКСТА"
        draw.text(((width-110)/4, (size[1]+50)), upper_text, (255, 255, 255), font = upper_font)
        lower_text = "СМЕШНОЙ СМЕШНОЙ СМЕШНОЙ СМЕШНОЙ СМЕШНОЙ"
        lower_font = ImageFont.truetype("times.ttf", size=upper_font.size-(upper_font.size//15))
        draw.text(((width - 110) / 3, (size[1]+50+upper_font.size)), lower_text, (255, 255, 255), font=lower_font)
        draw.rectangle(((pic_x-2,pic_y-2),(pic_x+size[0]+2,pic_y+size[1]+2)),fill=None,outline='white')
        dem.show()




    """with Image.open(dem_empty) as dem:
        dem.load()
        print(dem.size)
        print(img.size)
        resize_value = round(math.sqrt(dem.size[0]  / img.size[0])**2 + (dem.size[1] / img.size[1]**2))
        dem = dem.reduce(resize_value)
        dem.paste(img, (round(62/resize_value), round(41/resize_value)))
        print(resize_value)
        dem.show()"""


class Demotivator():
    def __init__(self, lower_text, higher_text, pic_url):
        self.lower_text = lower_text
        self.higher_text = higher_text
        self.pic_url = pic_url
    def demotivate(self):
        pass



