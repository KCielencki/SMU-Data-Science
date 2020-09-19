import csv
import os

inputFile = os.path.join(r"PyBank\\Resources", r"budget_data.csv")

#Tracking financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

#Reading CSV and converting to dictionaries
with open(inputFile) as financial_data:
    reader = csv.reader(financial_data)

    #Reading header row
    header = next(reader)

    #Extracting first row
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        #Tracking the total
        total_months += 1
        total_net += int(row[1])

        #Tracking the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        #Calculating the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #Calculating greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#Calculating the Avg Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

#Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Printing output to terminal
print(output)

#Exporting the results to text file
outputFile = os.path.join(r"PyBank\\Resources", r"output.txt")
with open(outputFile, "w") as txt_file:
     txt_file.write(output)