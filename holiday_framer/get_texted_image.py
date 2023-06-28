from PIL import Image

import vars
from holiday_framer.fontimg import generate_fontimg


def get_texted_from(image_path: str, text: str, font: str = None, fontsize: int = None, density: int = None):
    cl = {}
    if font:
        cl["font"] = font
    if fontsize:
        cl["fontsize"] = fontsize
    if density:
        cl["density"] = density
    extra_layer = generate_fontimg(text, **cl)
    if text != "В ОТПУСКЕ":
        extra_layer.save(f"avatars/layer_{vars.layer_counter}.png")
    vars.layer_counter += 1

    with Image.open(image_path) as img:
        img.load()

    if img.size[0] > img.size[1]:
        img = img.crop(((img.size[0] - img.size[1]) // 2, 0, (img.size[0] + img.size[1]) // 2, img.size[1]))
    elif img.size[0] < img.size[1]:
        img = img.crop((0, (img.size[1] - img.size[0]) // 2, img.size[0], (img.size[1] + img.size[0]) // 2))

    crop_size = max(img.size)
    front = extra_layer.resize((crop_size, crop_size))
    img.paste(front, (0, 0), front)
    print(img.size)

    return img
