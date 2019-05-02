from PIL import Image
from math import ceil
import os

curr_layer = ""
skin_color = (0.0, 1.0, 1.0, 1.0)
mouth_style = 1
hair_style = 1
hair_color = (1.0, 0.0, 1.0, 1.0)
back_color = (1.0, 1.0, 0.0, 1.0)
beard_style = 1
beard_color = (1.0, 0.5, 0.5, 1.0)
eyes_style = 1
eyes_color = (0.5, 0.5, 0.0, 1.0)

img = Image.new('RGB', (256, 256), "WHITE")
pixels = img.load()
blueprint_data = []


def background(back_color):
    back_color = [int(ceil(color*255)) for color in back_color]
    back_color = back_color[0:3]
    back_color = tuple(back_color)
    for i in range(256):
        for j in range(256):
            pixels[i, j] = back_color


def skin(skin_color):
    skin_color = [int(ceil(color*255)) for color in skin_color]
    skin_color = skin_color[0:3]
    skin_color = tuple(skin_color)
    blueprint = blueprint_data['Face']
    for i in range(256):
        for j in range(256):
            if blueprint[i][j] == '1':
                pixels[i, j] = skin_color


def eye(eye_style, eye_color):
    eye_color = [int(ceil(color*255)) for color in eye_color]
    eye_color = eye_color[0:3]
    eye_color = tuple(eye_color)
    blueprint = blueprint_data['Eyes'+str(eye_style)]
    for i in range(256):
        for j in range(256):
            if blueprint[i][j] == '1':
                pixels[i, j] = eye_color
            elif blueprint[i][j] == 2:
                pixels[i, j] = tuple([255, 255, 255])


def hair(hair_style, hair_color):
    hair_color = [int(ceil(color*255)) for color in hair_color]
    hair_color = hair_color[0:3]
    hair_color = tuple(hair_color)
    blueprint = blueprint_data['Hair' + str(hair_style)]
    for i in range(256):
        for j in range(256):
            if blueprint[i][j] == '1':
                pixels[i, j] = hair_color


def beard(beard_style, beard_color):
    beard_color = [int(ceil(color*255)) for color in beard_color]
    beard_color = beard_color[0:3]
    beard_color = tuple(beard_color)
    blueprint = blueprint_data['Beard' + str(beard_style)]
    for i in range(256):
        for j in range(256):
            if blueprint[i][j] == '1':
                pixels[i, j] = beard_color


def mouth(mouth_style):
    blueprint = blueprint_data['Mouth' + str(mouth_style)]
    for i in range(256):
        for j in range(256):
            if blueprint[i][j] == '1':
                pixels[i, j] = tuple([255, 255, 255])


def save_image(name):
    img.save(os.path.join(os.getcwd(), str(name) + ".png"), "png")


def save_image_2(name):
    img.save(os.path.join(os.getcwd() + "/saved", str(name) + ".png"), "png")


def generate():
    print(skin_color)

    background(back_color)
    skin(skin_color)
    hair(hair_style, hair_color)
    eye(eyes_style, eyes_color)
    beard(beard_style, beard_color)
    mouth(mouth_style)
