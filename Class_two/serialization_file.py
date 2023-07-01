import csv

# read from csv file
with open('student.csv') as file:
    reader = csv.reader(file)
    next(reader) # skip the first line
    for datarow in reader:
        print(datarow)


# write to an existing csv
with open('student.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Jadon Sancho', 'B4890', 'No department'])

# create and write to a csv
record = [
    ['item', 'qty', 'cost'],#header
    ['apple', 10, 12.30],
    ['spinach', 1, 2.30],
    ['black plums', 10, 4.99],
    ['apricots', 2, 4.99]
]
with open('groceries.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in record:
        writer.writerow(row)

with open('groceries_b.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(record) # any iterable