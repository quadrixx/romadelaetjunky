import requests
def get_gif(name):  # PEP8: lower_case_names for functions
    #находит в теноре рандомную хуету вместо нужной гифки и возвращает её юрл
    key = 'AIzaSyAaxn_f4rZAW89i65kxc4jNxFDx414_gtU'
    result = requests.get(f'https://tenor.googleapis.com/v2/search?q={name}&key={key}&locale=ru_RU&limit=10')
    data = result.json()
    url = data["results"][0]['media_formats']['gif']["url"]
    return url
def di(url):
    # скачивает гифку по юрлу(без хуйни)
    img_data = requests.get(url).content
    with open('image.gif', 'wb') as handler:
        handler.write(img_data)

def tenor_gif_handler(link):
    #вырезает из дискордовской ссылки название гифки по которому её по идее можно найти через гет гиф
    #по факту хуй там плавал, он находит рандомную хуету
    gif_name = link[23:-13]
    return gif_name

