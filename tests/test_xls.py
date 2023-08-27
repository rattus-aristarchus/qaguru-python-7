import xlrd
import os
from conftest import RESOURCES_DIR, XLS_NAME


def test_xls():
    xls_path = os.path.join(RESOURCES_DIR, XLS_NAME)
    book = xlrd.open_workbook(xls_path)

    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество колонок  {sheet.ncols}')
    print(f'Количество строк    {sheet.nrows}')
    test_cell = sheet.cell_value(rowx=3, colx=2)
    print(f'Пересечение строки и столбца {test_cell}')
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

    assert book.nsheets == 1
    assert book.sheet_names()[0] == "Sheet1"
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert test_cell == "Gent"
