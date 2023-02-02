"""This file contains utility functions for purposes like to get data from
file, create DB tables, etc"""
import csv
from django.core.exceptions import ValidationError
from ads.models import AdsModel, CategoryModel, models
from constants import ADS_FILE, CATEGORIES_FILE
# -----------------------------------------------------------------------


def load_csv(filename: str) -> list[dict]:
    """This function loads data from a csv file

    :param filename: the name of the csv file
    :return: a list of dictionaries
    """
    with open(filename, encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        result = []

        for row in reader:
            if 'is_published' in row:
                row['is_published'] = row['is_published'].capitalize()
            result.append(row)

    return result


def fill_up_database() -> None:
    """This function fills up the database with data from csv files"""
    advertisements = load_csv(ADS_FILE)
    categories = load_csv(CATEGORIES_FILE)
    fill_table(AdsModel, advertisements)
    fill_table(CategoryModel, categories)


def fill_table(model: type[models.Model], data: list[dict]) -> None:
    """This function serves to fill a single table by provided data

    :param model: the django model
    :param data: a list of dictionaries
    """
    for row in data:
        new_model = model(**row)
        try:
            new_model.full_clean()
            new_model.save()
        except ValidationError as e:
            print(f'Ошибка валидации данных {e}')
