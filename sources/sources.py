import collections
import datetime
import argparse
import os
import pandas


def get_path_excel_file(path):
    parser = argparse.ArgumentParser(
        description=
        """Запуск сайта: команда `python3 main.py`.
        
        Если вы не меняли файл wine.xlsx, или изменили его
        в папке source проекта, запустите сайт командой `python3 main.py`.
        Если вы создали новый файл excel, укажите путь к файлу в команде 
        запуска: `python3 main.py -p ./путь/к/файлу.xlsx`.
        Новый файл excel будет автоматически сохранен в папке source 
        проекта под именем wine.xlsx для использования по умолчанию.
        Перейдите на сайт по адресу http://127.0.0.1:8000.
        """
    )
    parser.add_argument('-p', '--path_excel', default=path, type=str)
    args = parser.parse_args()
    new_path = args.path_excel

    if os.path.exists(new_path):
        os.replace(new_path, path)

    return path


def transform_excel_into_products_list(path_excel_file):
    excel_data = pandas.read_excel(
        get_path_excel_file(path_excel_file),
        keep_default_na=False).to_dict(orient='records')

    products_list = collections.defaultdict(list)
    for data in excel_data:
        products_list[data['Категория']].append(data)

    return sorted(products_list.items())


def count_age_company():
    today = datetime.datetime.today().year
    year_company_foundation = 1920
    age = today - year_company_foundation
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'
