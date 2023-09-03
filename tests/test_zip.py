import pytest
import zipfile

import os

from conftest import RESOURCES_DIR, PDF_NAME, XLS_NAME, XLSX_NAME, ZIP_NAME


def test_zip():
    file_0 = os.path.join(RESOURCES_DIR, PDF_NAME)
    file_1 = os.path.join(RESOURCES_DIR, XLS_NAME)
    file_2 = os.path.join(RESOURCES_DIR, XLSX_NAME)
    zip_path = os.path.join(RESOURCES_DIR, ZIP_NAME)
    paths_to_files = [file_0, file_1, file_2]

    with zipfile.ZipFile(zip_path, mode="w") as archive:
        for filename in paths_to_files:
            archive.write(filename)

        names_in_zip = archive.namelist()
        filenames = [PDF_NAME, XLS_NAME, XLSX_NAME]

        for name in names_in_zip:
            assert os.path.basename(name) in filenames

        os.remove(zip_path)
