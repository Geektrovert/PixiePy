import csv
import os


def get_filenames():
    file_paths = os.listdir(os.path.abspath(
        os.path.join(os.getcwd(), 'blueprints')))
    file_paths = [os.path.join(os.getcwd(), 'blueprints', filename)
                  for filename in file_paths]
    return file_paths


def read_file_data(filenames):
    data_dict = {}
    data_list = []
    namelist = []
    for filename in filenames:
        data = []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            f.close()
        namelist.append(filename.split('/')[-1].strip('.csv'))
        data_list.append(data)
    data_dict = dict(zip(namelist, data_list))
    return data_dict


def get_data():
    filenames = get_filenames()
    data = read_file_data(filenames)
    return data
