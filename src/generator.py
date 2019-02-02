import PIL
import imagehash
import os


def __generate_new_256pixel_image__():
    return PIL.Image.new("RGB", (256, 256), "WHITE")


def __hex2rgb__(hex_value):
    hex_value = hex_value.strip('#')
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2 ,4))


def __save_image__(img):
    print(type(img))
    name = imagehash.average_hash(img)
    img.save(os.path.join(os.getcwd(), str(name) + ".png"), "png")


def generate_image(template, palette, save_image = True):
    img = __generate_new_256pixel_image__()
    pixels = img.load()
    rgb = [__hex2rgb__(hex_value) for hex_value in palette]

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = rgb[template[j][i]]
    
    if save_image is True:
        __save_image__(img)

    img.show()
