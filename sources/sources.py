import collections
import datetime

import pandas

wine_excel_data = pandas.read_excel('./sources/wine.xlsx').to_dict(orient='records')


def get_excel():
    result = collections.defaultdict(list)
    for i in wine_excel_data:
        result[i['Категория']].append(i)
    return result


def get_age():
    today = datetime.date.today()
    age = today.year - datetime.datetime(1920, 1, 1).year
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'
