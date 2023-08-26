import os
import pypdf

from conftest import RESOURCES_DIR


def test_pdf():
    pdf_path = os.path.join(RESOURCES_DIR, 'docs-pytest-org-en-latest.pdf')
    reader = pypdf.PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    # print(number_of_pages)
    # print(first_page)
    print(text)
    count = 0
    for image_file in first_page.images:
        with open(str(count) + image_file.name, 'wb') as fp:
            fp.write(image_file.data)
            count += 1

    assert number_of_pages == 412
    assert text[:20] == "pytest Documentation"
    assert count == 1
