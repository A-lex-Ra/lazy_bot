from PIL import Image, ImageDraw, ImageFont
import vars

RESOLUTION = 6


def generate_fontimg(text: str = 'В ОТПУСКЕ', font: str = vars.fonts[0], fontsize: int = 200, density: int = 137):
    print(text, font, fontsize, density)
    # Создаем объект со шрифтом
    font = ImageFont.truetype(f"holiday_framer/{font}", size=fontsize*RESOLUTION)
    print(font.getsize(text), "fontbounds")
    size = int(font.getsize(text)[0] * 1.1)
    im = Image.new('RGBA', (size, size), color=(0, 0, 0, density))

    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (im.size[0] // 2, im.size[1] // 2),
        text,
        anchor="mm",
        # Добавляем шрифт к изображению
        font=font,
        fill='#FFFFFF')
    return im
