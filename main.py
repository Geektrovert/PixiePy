from src import reverse
import os
import PIL

def get_file_list():
    files = os.listdir(os.path.abspath('blueprints/'))
    files = [os.path.abspath(os.path.join("blueprints", f)) for f in files if f.endswith('.png')]
    return files

def main():
    files = get_file_list()
    reverse.read_blueprint_files(files)

if __name__ == "__main__":
    main()
