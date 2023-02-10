"""This file contains utility functions for purposes like to get data from
file, create DB tables, etc"""
import csv
import json
from typing import Union
from django.core.exceptions import ValidationError
from ads.models import Ads, Category, models
from constants import ADS_FILE, CATEGORIES_FILE, USERS_FILE, LOCATIONS_FILE
from users.models import User, Location
# -----------------------------------------------------------------------


def load_csv(filename: str) -> list[dict]:
    """This function loads data from a csv file

    :param filename: the name of the csv file
    :return: a list of dictionaries
    """
    with open(filename, encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        return list(reader)


def fill_up_database() -> None:
    """This function fills up the database with data from csv files"""
    advertisements = load_csv(ADS_FILE)
    categories = load_csv(CATEGORIES_FILE)
    users = load_csv(USERS_FILE)
    locations = load_csv(LOCATIONS_FILE)

    fill_table(Ads, advertisements)
    fill_table(Category, categories)
    fill_table(User, users)
    fill_table(Location, locations)


def fill_table(model: type[models.Model], data: list[dict]) -> None:
    """This function serves to fill a single table by provided data
    :param model: the django model
    :param data: a list of dictionaries
    """
    for row in data:

        if 'is_published' in row:
            row['is_published'] = row['is_published'].capitalize()
        new_model = model(**row)

        try:
            new_model.full_clean()
            new_model.save()

        except ValidationError as e:
            print(f'Ошибка валидации данных {e}')


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

        if 'is_published' in row:
            row['is_published'] = row['is_published'].capitalize()

        pk = row.pop('id')
        new_row = {'fields': row, 'model': model_path, 'pk': int(pk)}
        result.append(new_row)

    save_to_json(result, json_file)

    return result


def save_to_json(obj: Union[list, dict], json_file: str) -> None:
    """This function saves data to a json file
    :param obj: the object to save such as a list or dict
    :param json_file: the name of the json file
    """
    with open(json_file, 'w', encoding='utf-8') as fout:
        json.dump(obj, fout, ensure_ascii=False)
