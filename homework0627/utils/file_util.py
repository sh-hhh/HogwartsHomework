import yaml


def get_datas():
    with open("../data/test_datas.yml", 'r', encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas