from Demotivor import demotivate
from PIL import Image, ImageSequence
import io


def demotivate_gif(upper_text, lower_text, gif_name: str):
    # спихжено отсюда https://github.com/python-pillow/Pillow/issues/3128
    im = Image.open(gif_name)
    frames = []
    for frame in ImageSequence.Iterator(im):
        frame = demotivate(upper_text, lower_text, frame)
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)
        frames.append(frame)
    frames[0].save('out.gif', save_all=True, append_images=frames[1:], duration=40, loop=0)
