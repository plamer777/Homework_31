"""This file contains utility functions to create json files from CSV"""
import csv
import json
from typing import Union
# -----------------------------------------------------------------------


def load_csv(filename: str) -> list[dict]:
    """This function loads data from a csv file

    :param filename: the name of the csv file
    :return: a list of dictionaries
    """
    with open(filename, encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        return list(reader)


def save_to_json(obj: Union[list, dict], json_file: str) -> None:
    """This function saves data to a json file
    :param obj: the object to save such as a list or dict
    :param json_file: the name of the json file
    """
    with open(json_file, 'w', encoding='utf-8') as fout:
        json.dump(obj, fout, ensure_ascii=False)


def create_json_from_csv(csv_file: str, json_file: str, model_path: str) -> \
        list[dict]:
    """This function serves to create a json file from a csv file
    :param csv_file: the name of the csv file
    :param json_file: the name of the json file to create
    :param model_path: the path to add in the json file
    :return: a list of dictionaries
    """
    json_data = load_csv(csv_file)
    result = []

    for row in json_data:
        for key, value in row.items():
            if value.isdigit():
                row[key] = int(value)
            else:
                try:
                    row[key] = float(value)
                except ValueError:
                    continue

        if 'is_published' in row:
            row['is_published'] = row['is_published'].capitalize()

        pk = row.pop('id')
        new_row = {'fields': row, 'model': model_path, 'pk': int(pk)}
        result.append(new_row)

    save_to_json(result, json_file)

    return result
