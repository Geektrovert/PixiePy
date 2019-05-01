from PIL import Image

img = Image.new('RGB', (256, 256), "WHITE")
pixels = img.load()
blueprint_data = []

def background(back_color):
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        pixels[i, j] = [back_color[0], back_color[1], back_color[2]]

def skin(skin_color):
    blueprint = blueprint_data['Face']
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i, j] = [skin_color[0], skin_color[1], skin_color[2]]

def eye(eye_style, eye_color):
    blueprint = blueprint_data['Eye'+str(eye_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i, j] = [eye_color[0], eye_color[1], eye_color[2]]
        elif blueprint[i][j] == 2:
            pixels[i, j] = [255, 255, 255]

def hair(hair_style, hair_color):
    blueprint = blueprint_data['Hair' + str(hair_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i,j] = [hair_color[0], hair_color[1], hair_color[2]]

def beard(beard_style, beard_color):
    blueprint = blueprint_data['Beard' + str(beard_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i,j] = [beard_color[0], beard_color[1], beard_color[2]]

def mouth(mouth_style):
    blueprint = blueprint_data['Mouth' + str(mouth_style)]
    for i, j in zip(range(img.size[0]), range(img.size[1])):
        if blueprint[i][j] == 1:
            pixels[i,j] = [255, 255, 255]

def generate(blueprint_data, skin_color, mouth_style, hair_style, hair_color, back_color, beard_style, beard_color, eye_color, eye_style):
    blueprint_data = blueprint_data
    background(back_color)
    skin(skin_color)
    hair(hair_style, hair_color)
    eye(eye_style, eye_color)
    beard(beard_style, beard_color)
    mouth(mouth_style)
    img.show()
