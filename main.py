
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from sources.sources import count_age_company, transform_excel_into_products_list


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
path_excel_file = './sources/wine.xlsx'

rendered_page = template.render(
    age_company=count_age_company(),
    products_list=transform_excel_into_products_list(path_excel_file),
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
