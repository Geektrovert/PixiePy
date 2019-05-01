from PIL import Image
import os
import csv


def detect(value):
    if value == 765:
        return 0
    elif value == 0:
        return 1
    return 2


def read_blueprint_files(file_paths):
    img_dict = {}
    img_list = []
    img_name_list = []
    for f in file_paths:
        img = Image.open(f).convert('RGB')
        img_list.append(img.load())
        img_name_list.append(f.split('/')[-1].strip('.png'))
    img_dict = dict(zip(img_name_list, img_list))

    blueprint_list = []
    for key, value in img_dict.items():
        blueprint = []
        for i in range(256):
            row = []
            for j in range(256):
                row.append(detect(sum(value[(i, j)])))
            blueprint.append(row)
        blueprint_list.append(blueprint)
    
    file_paths = [filename.replace('.png', '.csv') for filename in file_paths]

    for filename, data in zip(file_paths, blueprint_list):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data);
