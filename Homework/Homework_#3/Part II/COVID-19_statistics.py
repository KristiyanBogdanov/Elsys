# Scrap data
import requests
from bs4 import BeautifulSoup

# Represent and save data
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages

# Others
from datetime import date


CASES_BY_AGE = 0
CASES_BY_MED_STAFF = 1
CASES_BY_AREA = 2
VACCINATED_BY_AREA = 3
TESTS_DATA = 4
CASES_BY_KIND_OF_TEST = 5


# Functions
def get_tables_html(url):
    src = requests.get(url).text
    soup = BeautifulSoup(src, "lxml")
    return soup.find_all("table")


def get_two_col_table_data(table):
    first_loop = True
    table_data = {
        "total": {},
        "new": {}
    }

    for tr_tag in table.find_all("tr"):
        if first_loop:
            first_loop = False
            continue

        key, *values = tr_tag.text.strip().split("\n")

        if len(values) == 1:
            values.append(0)

        try:
            values = list(map(int, values))
        except ValueError:
            for idx, value in enumerate(values):
                if value == "-":
                    values[idx] = 0
                    continue
                values[idx] = int(value)

        table_data["total"][key] = values[0]
        table_data["new"][key] = values[1]

    return table_data


def get_table_data(table):
    first_loop = True
    table_data = {}

    for tr_tag in table.find_all("tr"):
        if first_loop:
            try:
                key, value = tr_tag.text.strip().split("\n")
                first_loop = False
                continue
            except ValueError:
                table_data = get_two_col_table_data(table)
                break

        key, value = tr_tag.text.strip().split("\n")
        table_data[key] = int(value)

    return table_data


def choose_areas(data):
    table_data = {}
    total = 0

    # All areas are too many, so you have to choose 5 of them
    areas = input("Избери 5 области: ").split(", ")

    for area in areas:
        table_data[area] = data[area]
        total += table_data[area]

    table_data["Общо"] = total
    return table_data


def unpack_data(data):
    data_keys = list(data.keys())
    data_values = list(data.values())

    keys = data_keys[:-1]
    values = data_values[:-1]
    total = f"{data_keys[-1]}: {data_values[-1]}"

    return keys, values, total


def make_pie_chart(data, title):
    keys, values, total = unpack_data(data)

    if not int(total.split()[1]):
        print("Total = 0")
        return None

    pyplot.style.use("bmh")
    fig = pyplot.figure(figsize=(10, 5))
    pyplot.suptitle(title, fontsize=14, fontweight='bold')

    pyplot.pie(values, autopct="%.1f%%", pctdistance=0.8)
    pyplot.legend(keys, title=total, fontsize=8.7, loc="upper left")
    pyplot.axis("equal")

    return fig


def make_bar_chart(data, title):
    keys, values, total = unpack_data(data)

    if not int(total.split()[1]):
        print("Total = 0")
        return None

    pyplot.style.use("default")
    fig = pyplot.figure(figsize=(10, 5))
    pyplot.suptitle(title, fontsize=14, fontweight="bold")

    pyplot.bar(keys, values, color="#3b0857")
    pyplot.grid(color="#676e68", linestyle="dashed", axis="y")

    return fig


def save_figures(figs):
    current_date = date.today().strftime("%d.%m.%Y")
    file_name = f"COVID-19 статистика - {current_date}.pdf"

    with PdfPages(file_name) as pdf:
        for fig in figs:
            if fig is not None:
                pdf.savefig(fig)


# Main
url = "https://coronavirus.bg/bg/statistika"

tables_html = get_tables_html(url)
tables_data = [get_table_data(table) for table in tables_html]

# That is ugly, but in the future I think to make simple UI
figs = [
    make_pie_chart(tables_data[CASES_BY_AGE], "Потвърдени случаи пo възраст"),
    make_bar_chart(choose_areas(tables_data[CASES_BY_AREA]["new"]), "Потвърдени случаи по области"),
    make_pie_chart(tables_data[TESTS_DATA]["new"], "Данни за лабораторни изследвания"),
    make_pie_chart(tables_data[CASES_BY_KIND_OF_TEST]["total"], "Потвърдени случаи според тип на лабораторно изследване"),
    make_bar_chart(tables_data[CASES_BY_MED_STAFF], "Потвърдени случаи по медицински персонал"),
    make_pie_chart(choose_areas(tables_data[VACCINATED_BY_AREA]["total"]), "Ваксинирани лица по oбласти")
]

save_figures(figs)
