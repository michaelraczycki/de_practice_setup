import json
import pandas as pd
from typing import TextIO
from glob import glob




def get_column_names(schemas: TextIO, dataset_name: str, sorting_key='column_name'):
    column_details = schemas[dataset_name]
    columns = sorted(column_details, key=lambda x: x[sorting_key])
    return [col['column_name'] for col in columns]

def get_dataset_name(path: str):
    return path.split('/')[4]

def load_dfs_from_csv(path: str, src_paths: str):
    src_paths = glob(src_paths)
    schemas = json.load(open(path, 'r'))
    dfs = {}
    for path in src_paths:
        dataset_name = get_dataset_name(path)
        order_columns = get_column_names(schemas, dataset_name)
        dfs[dataset_name] = pd.read_csv(path, names=order_columns)

    return dfs

def save_to_json(datasets: dict, path: str):
    for key, value in datasets.items():
        value.to_json(path + key + '.json', orient='records')

if __name__ == '__main__':
    save_to_json(load_dfs_from_csv('../data/retail_data/schemas.json', '../data/retail_data/CSV/*/*'), '../data/transformed_datafiles/JSON/')
