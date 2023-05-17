from PIL import Image, ImageFont, ImageDraw
import requests
import discord
from discord.ext import commands


def text_size(text, font):
    #возвращает примерный размер текста по горизонтали и вертикали в пикселях
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text).getbbox()[2]
    text_height = font.getmask(text).getbbox()[3] + descent

    return text_width, text_height
def pic_center(left, upper, width, height):
    #возвращает координаты центра картинки
    x = left + (width/2)
    y = upper + (height/2)
    return x, y
def di(url):
    #сохраняет картинку по юрлу под именем image.jpg
    img_data = requests.get(url).content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_data)


def demotivate(upper_text, lower_text, pic_url):
    di(pic_url)
    filename = 'image.jpg'
    dem_empty = "black.png"
    with Image.open(filename) as img:
        img.load()
        with Image.open(dem_empty) as dem:
            dem.load()
            size = img.size  # размер картинки внутри демотиватора

            # ниже вычисление размера всего демотиватора
            width = size[0] + size[0] * 0.4
            height = size[1] + size[1] * 0.4
            while width > 2000 or height > 2000:
                print('img reduced')
                img = img.reduce(2)
                size = img.size
                width = size[0] + size[0] * 0.4
                height = size[1] + size[1] * 0.4
            dem = dem.crop((0, 0, width, height))  # вырезаем фон для демотиватора
            draw = ImageDraw.Draw(dem)

            # ниже координаты верхнего левого угла картинки внутри демотиватора
            pic_x = round(width / 2 - size[0] / 2)
            pic_y = round(height / 2 - size[1] / 2 - height / 10)
            img_center = pic_center(pic_x, pic_y, size[0], size[1])
            dem.paste(img, (pic_x, pic_y))
            # ниже рисует белую рамку вокруг картинки
            draw.rectangle(((pic_x - 2, pic_y - 2), (pic_x + size[0] + 2, pic_y + size[1] + 2)), fill=None,outline='white')
            # дальше создание с текста
            upper_font_size = round(width / (len(upper_text) * 0.5))
            upper_font = ImageFont.truetype("times.ttf", size=upper_font_size)
            upper_text_size = text_size(upper_text, upper_font)

            # костыль
            while upper_text_size[1] > ((height - size[1] - pic_y - upper_text_size[1] * 2)) or upper_text_size[ 0] > width:
                upper_font_size = upper_font_size - 1
                upper_font = ImageFont.truetype("times.ttf", size=upper_font_size)
                upper_text_size = text_size(upper_text, upper_font)

            upper_text_x = img_center[0] - (upper_text_size[0] / 2)
            upper_text_y = pic_y + size[1]*1.02
            draw.text((upper_text_x, upper_text_y), text=upper_text, color=(255, 255, 255), font=upper_font)

            lower_font_size = round((upper_font.size - round(upper_font.size / (2 + len(lower_text)*0.5))))
            lower_font = ImageFont.truetype("times.ttf", size=lower_font_size)
            lower_text_size = text_size(lower_text, lower_font)
            while lower_text_size[1] > ((height - size[1] - pic_y - lower_text_size[1] * 2)) or lower_text_size[0] > width:
                lower_font_size = lower_font_size - 1
                lower_font = ImageFont.truetype("times.ttf", size=lower_font_size)
                lower_text_size = text_size(lower_text, lower_font)
            lower_text_x = img_center[0] - (lower_text_size[0] / 2)
            lower_text_y = upper_text_y + lower_text_size[1] + upper_text_size[1]/2
            draw.text((lower_text_x, lower_text_y), text=lower_text, color=(255, 255, 255), font=lower_font)
            dem.save('demotivated.png')
            #dem.show()
#link = "https://cdn.discordapp.com/attachments/1107399217313501345/1108372212962033674/nix.jpg"
#demotivate('dsf',"dxc",link)
#комментарии для тестов