from openpyxl import load_workbook
import os

from conftest import RESOURCES_DIR
# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_xlsx():
    xlsx_path = os.path.join(RESOURCES_DIR, "file_example_XLSX_50.xlsx")
    book = load_workbook(xlsx_path)
    sheet = book.active
    test_cell = sheet.cell(row=3, column=2)
    print(test_cell.value)

    assert test_cell.value == "Mara"
#    assert
