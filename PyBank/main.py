import os
import csv

# path to input csv
budget_data_path = os.path.join("Resources", "budget_data.csv")
doc = open("main.txt","w")

# list for storing the columns in our output file
data_months = list()
data_profit = list()
data_change = list()

# open input csv and read columns of interest into our lists
with open(budget_data_path, "r", encoding="utf-8") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        months = row[0]
        profit = int(row[1])

        data_months.append(months)
        data_profit.append(profit)

output_data = zip(data_months, data_profit)

# number of months in data set
total_months = len(data_months)
    
# net total of profit and loss
total_profit = 0
for profit in data_profit:
        total_profit += profit

print("Financial Analysis")
print("-------------------")
print("Total Months:", total_months)
print("Total Profits: $", total_profit)

# changes over the period
for i in range(1,len(data_profit)):
    changes = (data_profit[i] - data_profit[i-1])
    data_change.append(float(changes))
total_changes = 0
for changes in data_change:
        total_changes += changes

# average of changes over the period
average_change = total_changes / (total_months-1)

# greatest movement dates and amounts
max_profit_change = max(data_change)
min_profit_change = min(data_change)
indexed_change_data = data_change.index
max_profit_change_date = str(data_months[indexed_change_data(max_profit_change)+1])
min_profit_change_date = str(data_months[indexed_change_data(min_profit_change)+1])

# output greatest movement data
print("Average changes in profit / loss: $", round(average_change,2))
print("Greatest Increase in Profit:", max_profit_change_date, "($", max_profit_change,")")
print("Greatest Decrease in Profit:", min_profit_change_date, "($", min_profit_change,")")

# print to main.txt file
print("Financial Analysis", file=doc)
print("-------------------", file=doc)
print("Total Months:", total_months, file=doc)
print("Total Profits: $", total_profit, file=doc)
print("Average changes in profit / loss: $", round(average_change,2),file=doc)
print("Greatest Increase in Profit:", max_profit_change_date, "($", max_profit_change,")",file=doc)
print("Greatest Decrease in Profit:", min_profit_change_date, "($", min_profit_change,")",file=doc)
doc.close()