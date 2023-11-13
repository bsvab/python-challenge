
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The changes in "Profit/Losses" over the entire period, and then the average of those changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period

line_title = 'Financial Analysis'
line_break = '----------------------------'
print(line_title)
print(line_break)

import os
import csv

csvpath = os.path.join('resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)    # skip header row
    
    # ====================================================================================================================
    # code to return the total months

    row_count = len(list(csvreader))
    line_total_months = f'Total Months: {row_count}'     # 1 row = 1 month, so count of rows is the count of months
    print(line_total_months)

    # ====================================================================================================================
    # code to return the total profit/loss

    # ////////// something about this section results in a total value of $0 and it should be $22,564,198 ...?

    total_profloss = 0

    for row in csvreader:
        profloss = int(row[1])
        total_profloss += profloss
    
    line_total_profloss = f'Total: ${total_profloss}'
    print(line_total_profloss)

    # \\\\\\\\\\

    # ====================================================================================================================
    # code to return the average change

    avg_profloss = total_profloss / row_count
    line_avg_profloss = f'Average Change: ${avg_profloss}'
    print(line_avg_profloss)

    # ////////// trying average via making a formula below instead...

    # def average(numbers):
    #     qty = len(numbers)
    #     total = 0
    #     for number in numbers:
    #         total += number
    #     return (total / qty) * 100

    # list_profloss = [row[1] for row[1] in csvreader]

    # avg_profloss = average(list_profloss)
    # print(f'Average Change: ${avg_profloss}')

    # \\\\\\\\\\ 

    # ====================================================================================================================
    # code to return the greatest increase and greatest decrease in profits

    # ////////// something wrong in this section = results in list_profloss remaining empty so min/max funcions don't work

    list_profloss = []

    # for row in csvreader:
    #     list_profloss.append(int(row[1]))
    # commenting out above 2 lines to try the below line instead...
    list_profloss = [row[1] for row[1] in csvreader]

    # \\\\\\\\\\

    min_profloss = min(list_profloss)
    max_profloss = max(list_profloss)

    line_max_profloss = f'Greatest Increase in Profits: (${max_profloss})'
    print(line_max_profloss)
    line_min_profloss = f'Greatest Decrease in Profits: (${min_profloss})'
    print(line_min_profloss)


# ====================================================================================================================
# code to write outputs to text file in analysis folder

analysis_path = os.path.join('analysis','analysis.txt')

lines = [line_title, '\n', line_break, '\n',
             line_total_months, '\n', line_total_profloss, '\n', line_avg_profloss, '\n', 
             line_max_profloss, '\n', line_min_profloss]

with open(analysis_path,'w') as text:
    text.writelines(lines)

