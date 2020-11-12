import collections
import datetime

import pandas


def get_excel():
    excel_data = pandas.read_excel('./sources/wine.xlsx').to_dict(orient='records')
    result = collections.defaultdict(list)
    for i in excel_data:
        result[i['Категория']].append(i)
    return collections.OrderedDict(sorted(result.items(), key=lambda t: t[0]))


def get_age():
    today = datetime.date.today()
    age = today.year - datetime.datetime(1920, 1, 1).year
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'
