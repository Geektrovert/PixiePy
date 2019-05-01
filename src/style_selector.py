from PIL import Image
from math import ceil

img = Image.new('RGB', (256, 256), "WHITE")
pixels = img.load()
blueprint_data = []

def background(back_color):
    back_color = [int(ceil(color*255)) for color in back_color]
    back_color = back_color[0:3]
    back_color = tuple(back_color)
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        pixels[i, j] = back_color

def skin(skin_color):
    skin_color = [int(ceil(color*255)) for color in skin_color]
    skin_color = skin_color[0:3]
    skin_color = tuple(skin_color)
    blueprint = blueprint_data['Face']
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i, j] = skin_color

def eye(eye_style, eye_color):
    eye_color = [int(ceil(color*255)) for color in eye_color]
    eye_color = eye_color[0:3]
    eye_color = tuple(eye_color)
    blueprint = blueprint_data['Eye'+str(eye_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i, j] = eye_color
        elif blueprint[i][j] == 2:
            pixels[i, j] = [255, 255, 255]

def hair(hair_style, hair_color):
    hair_color = [int(ceil(color*255)) for color in hair_color]
    hair_color = hair_color[0:3]
    hair_color = tuple(hair_color)
    blueprint = blueprint_data['Hair' + str(hair_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i,j] = hair_color

def beard(beard_style, beard_color):
    beard_color = [int(ceil(color*255)) for color in beard_color]
    beard_color = beard_color[0:3]
    beard_color = tuple(beard_color)
    blueprint = blueprint_data['Beard' + str(beard_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i,j] = beard_color

def mouth(mouth_style):
    blueprint = blueprint_data['Mouth' + str(mouth_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i,j] = [255, 255, 255]

def generate(data, skin_color, mouth_style, hair_style, hair_color, back_color, beard_style, beard_color, eye_color, eye_style):
    blueprint_data = data
    background(back_color)
    skin(skin_color)
    hair(hair_style, hair_color)
    eye(eye_style, eye_color)
    beard(beard_style, beard_color)
    mouth(mouth_style)
    img.show()
