import csv
import os


class palette_reader:

    def __init__(self, path):
        self.__path = path
        self.__data = []


    def __read_from_csv__(self, path):
        raw_data = []
        try:
            with open(path, 'r') as csv_file:
                data_reader = csv.reader(csv_file, delimiter=',')
                for row in data_reader:
                    raw_data.append(list(row))
                csv_file.close()
            print("Data extraction from palette: " + str(path.split('/')[-1]) + " successful!")
        except expression as identifier:
            print("Data extraction unsuccessful!")
        finally:
            return raw_data


    def __read_palette__(self, path):
        palette = []
        if(os.path.exists(path)):
            palette = self.__read_from_csv__(path)
        else:
            print("Path: '" + str(path) + "' doesn't exist.")
        return palette
    

    def __get_path__(self):
        return self.__path


    def get_palette(self):
        self.__data = self.__read_palette__(self.__path)
        return self.__data[0]


class template_reader(palette_reader):

    def __init__(self, path):
        super().__init__(path)


    def __clean_data(self, raw_data):
        clean_data = []
        for row in raw_data:
            clean_row = [int(individual_data.strip(' ')) for individual_data in row if isinstance(individual_data, str)]
            clean_data.append(clean_row)
        return clean_data

    def __read_template__(self, path):
        return super().__read_palette__(path)


    def get_template(self):
        raw_template = self.__read_template__(super().__get_path__())
        clean_template = self.__clean_data(raw_template)
        return clean_template
