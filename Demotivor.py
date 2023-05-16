from PIL import Image, ImageFont, ImageDraw
import requests
import discord
from discord.ext import commands


def text_size(font_size, text):
    #возвращает примерный размер текста по горизонтали и вертикали в пикселях
    upper_case = 0
    lower_case = 0
    for i in text:
        if i.isupper(): upper_case += 1
        else: lower_case += 1
    x = 0.47 * lower_case * font_size + 0.64 * upper_case * font_size
    y = font_size
    return x, y
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
            height = size[1] + size[1] * 0.8
            dem = dem.crop((0, 0, width, height))  # вырезаем фон для демотиватора
            draw = ImageDraw.Draw(dem)

            # ниже координаты верхнего левого угла картинки внутри демотиватора
            pic_x = round(width / 2 - size[0] / 2)
            pic_y = round(height / 2 - size[1] / 2 - height / 10)
            img_center = pic_center(pic_x, pic_y, size[0], size[1])
            dem.paste(img, (pic_x, pic_y))
            # ниже рисует белую рамку вокруг картинки
            draw.rectangle(((pic_x - 2, pic_y - 2), (pic_x + size[0] + 2, pic_y + size[1] + 2)), fill=None,outline='white')
            #[eq
            # дальше создание с текста
            upper_font_size = round(width / (len(upper_text) * 0.5))
            upper_font = ImageFont.truetype("times.ttf", size=upper_font_size)
            upper_text_size = text_size(upper_font_size, upper_text)
            # костыль
            while upper_text_size[1] > ((height - size[1] - pic_y - upper_text_size[1] * 2)):
                upper_text_size = text_size(upper_font_size, upper_text)
                upper_font_size = upper_font_size - 1
            upper_font = ImageFont.truetype("times.ttf", size=upper_font_size)

            draw.text((img_center[0] - (upper_text_size[0] / 2), pic_y + size[1] + size[1] / 20), text=upper_text,
                      color=(255, 255, 255), font=upper_font)

            lower_font_size = upper_font.size - (upper_font.size // 50)
            lower_font = ImageFont.truetype("times.ttf", size=lower_font_size)
            lower_text_size = text_size(lower_font_size, lower_text)
            draw.text(
                (img_center[0] - (lower_text_size[0] / 2), pic_y + size[1] + lower_text_size[1] + size[1] / 15),
                text=lower_text, color=(255, 255, 255), font=lower_font)
            dem = dem.save("demotivated.png")