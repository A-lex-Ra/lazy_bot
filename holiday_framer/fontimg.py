from PIL import Image, ImageDraw, ImageFont
import vars


def generate_fontimg(text: str = 'В ОТПУСКЕ', font: str = vars.fonts[0], fontsize: int = 300, density: int = 137):
    print(text, font, fontsize, density)
    im = Image.new('RGBA', (1920, 1920), color=(0, 0, 0, density))
    # Создаем объект со шрифтом
    font = ImageFont.truetype(f"holiday_framer/{font}", size=fontsize)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (im.size[0] // 2, im.size[1] // 2),
        text,
        anchor="mm",
        # Добавляем шрифт к изображению
        font=font,
        fill='#FFFFFF')
    return im
