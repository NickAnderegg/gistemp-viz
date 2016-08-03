import csv
import pathlib

data = pathlib.Path('tempdata.csv')
with data.open('r', encoding='utf-8', newline='') as f:
    csvreader = csv.reader(f, delimiter=',')

    cleaned = []
    for row in csvreader:
        row = [x.strip() for x in row]
        cleaned.append(row[:-1])

data = pathlib.Path('cleandata.js')
with data.open('w', encoding='utf-8', newline='') as f:
    # csvwriter = csv.writer(f, delimiter=',', lineterminator='\n')
    # csvwriter.writerows(cleaned)

    f.write('var temp_data = [{\n')

    labels = cleaned[0]
    for ix, row in enumerate(cleaned[1:]):
        row_string = []
        for jx, col in enumerate(row):
            if '*' not in col:
                row_string.append('        "{}": {},\n'.format(labels[jx], col))
            else:
                row_string.append('        "{}": {},\n'.format(labels[jx], 'null'))

        f.write(''.join(row_string)[:-2])
        f.write('\n')
        if ix != len(cleaned[1:])-1:
            f.write('    },\n    {\n')
        else:
            f.write('    }\n]')
