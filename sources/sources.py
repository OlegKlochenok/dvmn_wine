import collections
import datetime
import argparse
import os
import pandas


def path_excel():
    parser = argparse.ArgumentParser(
        description="""
                     Если вы не меняли файл wine.xlsx, или изменили его в папке source проекта, 
                     запустите сайт командой 
                     `python3 main.py`
                     Если вы создали новый файл excel, укажите путь к файлу в команде запуска: 
                     `python3 main.py -p ./путь/к/файлу.xlsx`
                     Новый файл excel будет автоматически сохранен в папке source проекта под 
                     именем wine.xlsx для использования по умолчанию.
                     Перейдите на сайт по адресу http://127.0.0.1:8000.
        """
    )
    parser.add_argument('-p', '--path_excel',
                        default='./sources/wine.xlsx',
                        help='полный путь к excel-файлу с данными для сайта в виде: "./путь/к/файлу"',
                        type=str)
    args = parser.parse_args()
    new_path = args.path_excel

    if not args:
        return args
    else:
        old_path = './sources/wine.xlsx'
        if os.path.exists(new_path):
            os.replace(new_path, "./sources/wine.xlsx")
        return old_path


def get_excel():
    excel_data = pandas.read_excel(path_excel()).to_dict(orient='records')
    #  Поправляем словарь Панды, где все None почему-то заполнены float nan, меняем на 0
    for obj in excel_data:
        for key in obj:
            if obj[key] != obj[key]:
                obj[key] = 0

    result = collections.defaultdict(list)
    for i in excel_data:
        result[i['Категория']].append(i)

    return sorted(result.items())


def get_age():
    today = datetime.date.today()
    year_company_founded = datetime.datetime(1920, 1, 1).year
    age = today.year - year_company_founded
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'
