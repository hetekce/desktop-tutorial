from PIL import Image, ImageDraw, ImageFont


def create_png(family_names):
    text_y_position = 800
    text_padding = 120
    image_width = 1920
    image_height = (len(family_names) * text_padding) + (text_y_position * 2)

    img = Image.new('RGB', (image_width, image_height), color=(58, 63, 68))
    draw = ImageDraw.Draw(img)

    fnt = ImageFont.truetype('arial.ttf', 100)

    for name in family_names:
        text_width, _ = draw.textsize(name, font=fnt)

        # zuerst 'x' value, dann 'y' position
        draw.text(((image_width - text_width) / 2, text_y_position), name, font=fnt, fill=(250, 250, 25))
        text_y_position += text_padding

    img.save('family_2.png')

    return img


unsere_familie = ['Emre Tekce', 'Adem Gormez',
                  'Alperen Bingol', 'Taner oztas']

create_png(unsere_familie)
