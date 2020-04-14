import csv

electioncsv = r"02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

with open(electioncsv) as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")
    csvHeader = next(csvReader)
    rowCount = sum(1 for row in csvReader)
    print("Total Votes: " + str(rowCount))