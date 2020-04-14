import csv

budgetcsv = r"02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

print("Financial Analysis:")
print("__________________")

with open(budgetcsv) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvReader)
    rowCount = sum(1 for row in csvReader)
    print("Number of Months: " + str(rowCount))

with open(budgetcsv) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvReader)
    total = 0
    for row in csvReader:
        total += int(row[1])
    print("Total Profit/Loss: " + str(total))