import yaml


def get_data(node):
    file_path = "./data/testdata.yml"
    with open(file_path, 'r', encoding="utf-8") as f:
        data = yaml.safe_load(f)[node]
    return data
