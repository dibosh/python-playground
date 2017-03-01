import json
import random


def create_row(company):
    row = []
    row.append(company)
    total = 0
    providers = ['Getty', 'Shutterstock', 'Twenty20'];
    for i in range(0, 3):
        r_usage = random.randrange(0, 300, 2)
        row.append(r_usage)
        total += r_usage
    row.append(total)
    return row


def create_rows():
    rows = []
    rows.append(["Client Name", "Getty", "Twenty20", "Shutterstock", "Total"])
    names = ['Monstar UK', 'Monstar US', 'NewsCred Blog', 'Facebook News', 'Prothom Aalo',
             'Devonport EA', 'Sanbilar', 'Schneider Electric', 'Bloomberg'];
    for name in names:
        row = create_row(name)
        rows.append(row)

    return json.dumps(rows, indent=4)


if __name__ == '__main__':
    print create_rows()
