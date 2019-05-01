import glob
import os
import data_reader as dreader
import resize
import generator


def print_data(template):
    if template is not None:
        for row in template:
            for data in row:
                print(data, end='')
            print("\n")


def print_data_size(template):
    if template is not None:
        print("Data size: " + str(len(template)) + " " + str(len(template[0])))


def get_template():
    path = "/templates/pacman_ghost_template.csv"
    # path = "/home/rafid/PycharmProjects/PixiePy/templates/pacman_ghost_template.csv"
    path = os.path.abspath(path)
    ghost_template = dreader.template_reader(path)
    return ghost_template.get_template()


def get_palette():
    path = "/templates/pacman_palette.csv"
    # path = "/home/rafid/PycharmProjects/PixiePy/templates/pacman_palette.csv"
    path = os.path.abspath(path)
    ghost_palette = dreader.palette_reader(path)
    return ghost_palette.get_palette()


if __name__ == "__main__":
    template = get_template()
    resized_template = resize.resize_template_for_256pixel(template)
    palette = get_palette()
    generator.generate_image(resized_template, palette)
