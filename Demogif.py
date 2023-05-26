import requests
from Demotivor import demotivate
from PIL import Image, ImageDraw, ImageSequence
import io
def get_gif(name:str):  # PEP8: lower_case_names for functions
    #находит в теноре рандомную хуету вместо нужной гифки и возвращает её юрл
    key = 'AIzaSyAaxn_f4rZAW89i65kxc4jNxFDx414_gtU'
    result = requests.get(f'https://tenor.googleapis.com/v2/search?q={name}&key={key}&locale=ru_RU&limit=10')
    data = result.json()
    url = data["results"][0]['media_formats']['gif']["url"]
    return url
def di(url:str):
    # скачивает гифку по юрлу(без хуйни)
    img_data = requests.get(url).content
    with open('image.gif', 'wb') as handler:
        handler.write(img_data)

def tenor_gif_handler(link:str):
    #вырезает из дискордовской ссылки название гифки по которому её по идее можно найти через гет гиф
    #по факту хуй там плавал, он находит рандомную хуету
    gif_name = link[23:-13]
    return gif_name

def demotivate_gif(upper_text, lower_text, gif_name:str):
    #спихжено отсюда https://github.com/python-pillow/Pillow/issues/3128
    im = Image.open(gif_name)
    frames = []
    for frame in ImageSequence.Iterator(im):
        frame = demotivate(upper_text, lower_text, frame)
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)
    frames[0].save('out.gif', save_all=True, append_images=frames[1:], duration=40, loop=0)


demotivate_gif("venomancer reaction", 'venomancer reaction', "image.gif")