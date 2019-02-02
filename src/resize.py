from itertools import repeat


def resize_template_for_256pixel(template):
    resized_template = []
    for row in template:
        resized_row = []
        for data in row:
            resized_row.extend(repeat(data, 16))
        count = 0
        for count in range(16):
            resized_template.append(resized_row)
    return resized_template
