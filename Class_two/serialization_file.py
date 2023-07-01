import csv

# read from csv file
with open('student.csv') as file:
    reader = csv.reader(file)
    next(reader) # skip the first line
    for datarow in reader:
        print(datarow)


# write to an existing csv
# create and write to a csv