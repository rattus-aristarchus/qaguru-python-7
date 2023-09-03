import pytest
import zipfile

import os

from conftest import RESOURCES_DIR, PDF_NAME, XLS_NAME, XLSX_NAME, ZIP_NAME


def test_zip():
    file_0 = os.path.join(RESOURCES_DIR, PDF_NAME)
    file_1 = os.path.join(RESOURCES_DIR, XLS_NAME)
    file_2 = os.path.join(RESOURCES_DIR, XLSX_NAME)
    zip_path = os.path.join(RESOURCES_DIR, ZIP_NAME)
    filenames = [file_0, file_1, file_2]

    with zipfile.ZipFile(zip_path, mode="w") as archive:
        for filename in filenames:
            archive.write(filename)

        names_in_zip = archive.namelist()

        for name in names_in_zip:
            assert get_proper_name(name) in filenames

        os.remove(zip_path)


def get_proper_name(name):
    return os.path.join(os.path.abspath(os.sep), name)
