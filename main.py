# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def get_age():
    date_of_foundation = datetime.date(year=1920,
                                       month=1, day=1)
    today = datetime.date.today()
    age = today.year - date_of_foundation.year
    if age == 1 or age % 100 == 1:
        return str(age) + ' год'
    if age == 2 or age % 100 == 2 or age % 100 == 3 or age % 100 == 4:
        return str(age) + ' года'
    else:
        return str(age) + ' лет'


rendered_page = template.render(
    age_company=get_age(),

    izabella_name='Изабелла',
    izabella_image='images/izabella.png',
    izabella_price='350 р.',
    izabella_sort='Сорт винограда - Изабелла',
    granat_name='Гранатовый браслет',
    granat_image='images/granatovyi_braslet.png',
    granat_price='350 р.',
    granat_sort='Сорт винограда - Мускат розовый',

)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
