import yaml


def get_data(file,node):
    file_path = "../data/"+file
    with open(file_path, 'r', encoding="utf-8") as f:
        data = yaml.safe_load(f)[node]
    return data
