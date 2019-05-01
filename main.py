from src import reverse
from src import App
from src import load_data
import time
import os
import PIL

def get_file_list():
    files = os.listdir(os.path.abspath('blueprints/'))
    files = [os.path.abspath(os.path.join("blueprints", f)) for f in files if f.endswith('.png')]
    return files

def extract():
    files = get_file_list()
    reverse.read_blueprint_files(files)


def run_app():
    App.MyMainApp().run()

def test_data_load():
    load_data.get_data()

if __name__ == "__main__":
    run_app()
