from PIL import Image, ImageFont, ImageDraw
import requests


def text_size(text, font):
    # возвращает примерный размер текста по горизонтали и вертикали в пикселях
    if text == "" or text == " ":
        return 0, 0
    ascent, descent = font.getmetrics()
    text_width = font.getmask(text).getbbox()[2]
    text_height = font.getmask(text).getbbox()[3] + descent
    return text_width, text_height


def pic_center(left, upper, width, height):
    # возвращает координаты центра картинки
    x = left + (width / 2)
    y = upper + (height / 2)
    return x, y


def di(url):
    # сохраняет картинку по юрлу под именем image.jpg
    img_data = requests.get(url).content
    with open('image.jpg', 'wb') as handler:
        handler.write(img_data)


def demotivate(upper_text, lower_text, file):
    # тут теперь типа перегрузка
    if type(file) == type("string"):
        # если на вход подается стока то это юрл картинки
        # это когда делаем демотиватор картинки
        di(file)
        filename = "image.jpg"
        img = Image.open(filename)
        img.load()
    else:
        # если это не строка то это кадр гифки из Demogif
        img = file
    size = img.size  # размер картинки внутри демотиватора
    # ниже вычисление размера всего демотиватора
    width = int(size[0] + size[0] * 0.2)
    height = int(size[1] + size[1] * 0.4)
    while width > 2000 or height > 2000:
        width = int(width / 2)
        height = int(height / 2)
    dem = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(dem)

    # ниже координаты верхнего левого угла картинки внутри демотиватора
    img_x = round(width / 2 - size[0] / 2)
    img_y = round(height / 2 - size[1] / 2 - height / 10)
    img_center = pic_center(img_x, img_y, size[0], size[1])
    dem.paste(img, (img_x, img_y))
    # ниже рисует белую рамку вокруг картинки
    draw.rectangle(((img_x - 2, img_y - 2), (img_x + size[0] + 2, img_y + size[1] + 2)), fill=None, outline='white')
    # дальше создание с текста
    upper_font_size = round(width / (len(upper_text) * 0.5))
    # файл со шрифтом должен быть в этой же папке
    upper_font = ImageFont.truetype("times.ttf", size=upper_font_size)
    upper_text_size = text_size(upper_text, upper_font)

    # ниже уменьшает шрифт чтобы текст если текст не влезает
    while upper_text_size[1] > (height - size[1] - img_y - upper_text_size[1] * 2) or upper_text_size[0] > width:
        upper_font_size = upper_font_size - 1
        upper_font = ImageFont.truetype("times.ttf", size=upper_font_size)
        upper_text_size = text_size(upper_text, upper_font)
    # координаты на которых будет расположен текст(это не левый верхний угол(это ваще хз что))
    upper_text_x = img_center[0] - (upper_text_size[0] / 2)
    upper_text_y = img_y + size[1] * 1.02
    draw.text((upper_text_x, upper_text_y), text=upper_text, color=(255, 255, 255), font=upper_font)

    # размеры шрифтов высчитываются по формулам выведенным методом тыка(как и всё остальное)
    lower_font_size = round((upper_font.size - round(upper_font.size / (2 + len(lower_text) * 0.5))))
    lower_font = ImageFont.truetype("times.ttf", size=lower_font_size)
    lower_text_size = text_size(lower_text, lower_font)
    # копия костыля сверху
    while lower_text_size[1] > (height - size[1] - img_y - lower_text_size[1] * 2) or lower_text_size[0] > width:
        lower_font_size = lower_font_size - 1
        lower_font = ImageFont.truetype("times.ttf", size=lower_font_size)
        lower_text_size = text_size(lower_text, lower_font)
    lower_text_x = img_center[0] - (lower_text_size[0] / 2)
    lower_text_y = upper_text_y + lower_text_size[1] + upper_text_size[1] / 2
    draw.text((lower_text_x, lower_text_y), text=lower_text, color=(255, 255, 255), font=lower_font)

    if type(file) == type("string"):
        # если был был юрл то картинка сохраняется
        dem.save('demotivated.png')
    else:
        # если это был кадр из гифки то его демотивированная версия
        # возвращается в демогиф
        return dem
    # dem.show()
# link = "https://sun3-21.userapi.com/impg/4Fp0xbWFmRlaw-EW449xSHmr_lW_M-jdaXYgJQ/fKD6ppr1cLY.jpg?size=829x1280
# &quality=96&sign=b6505841d6156544eac8dbabfe5c44aa&type=album" demotivate('test', "test", link) комментарии для тестов
