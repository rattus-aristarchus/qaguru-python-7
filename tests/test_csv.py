import csv
import os

from conftest import RESOURCES_DIR, CSV_NAME


def test_csv():
    csv_path = os.path.join(RESOURCES_DIR, CSV_NAME)

    with open(csv_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_path) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        result = []
        print("\n")
        for row in csvreader:
            print(row)
            result.append(row)

        assert result[0] == ["Bonny", "Born", "Peter"]
        assert result[1] == ["Alex", "Serj", "Yana"]

    os.remove(os.path.abspath(csv_path))
