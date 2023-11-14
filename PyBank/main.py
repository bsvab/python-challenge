
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The changes in "Profit/Losses" over the entire period, and then the average of those changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period

# this comment is typical for all "line_descriptor" variables in the following code - saving all lines to be eventually printed to the .txt file as 
    # variables so I can use them both to print to terminal and to .txt without typing it out twice

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
    # code to return the total months, return the total profit/loss, and generate a dictionary of the profit/loss change values

    total_profloss = 0  # establishing total profit/loss amount accumulator
    row_count = 0   # establishing row (month) count accumulator
    profloss_change = 0     # establishing variable for the profit/loss deltas to be populated into a dict in the for loop
    list_profloss_change = []   # establishing empty list to pull all the profit/loss change values into in order to feed into sum/min/max formulas later 
    dict_profloss_change = {}   # establish empty dict to receive the profit/loss deltas and dates to use to pull the date associated w/ the min/max later

    for row in csvreader:
        if row_count >= 1:
            profloss_change = int(row[1])-profloss  # calc profloss_change and apply to variable
            list_profloss_change.append(profloss_change)    # populate list
            dict_profloss_change["date"] = row[0]   # populate first key in dict
            dict_profloss_change["pl-change"] = profloss_change     # populate second key in dict
        profloss = int(row[1])  # apply profloss value to variable
        total_profloss += profloss  # increase accumulator for total_profloss
        row_count += 1  # increase accumulator for row (month) count

    line_total_months = f'Total Months: {row_count}'     # 1 row = 1 month, so count of rows is the count of months
    print(line_total_months)
    line_total_profloss = f'Total: ${total_profloss}'
    print(line_total_profloss)

    # ====================================================================================================================
    # code to return the average change

    avg_profloss = round((sum(list_profloss_change) / (row_count - 1)),2)
    line_avg_profloss = f'Average Change: ${avg_profloss}'
    print(line_avg_profloss)

    # ====================================================================================================================
    # code to return the greatest increase and greatest decrease in profits + associated dates

    min_profloss = min(list_profloss_change)   # identify min change
    min_profloss_date = [key for key in dict_profloss_change['pl-change'] == min_profloss]  # identify date associated w/ min change

    max_profloss = max(list_profloss_change)   # identify max change
    max_profloss_date = [key for key in dict_profloss_change['pl-change'] == max_profloss]  # identify date associated w/ max change

    # print all the things...
    line_max_profloss = f'Greatest Increase in Profits: {max_profloss_date} (${max_profloss})'
    print(line_max_profloss)
    line_min_profloss = f'Greatest Decrease in Profits: {min_profloss_date} (${min_profloss})'
    print(line_min_profloss)

# ====================================================================================================================
# code to write outputs to text file in analysis folder

analysis_path = os.path.join('analysis','analysis.txt')

lines = [line_title, '\n', line_break, '\n',
             line_total_months, '\n', line_total_profloss, '\n', line_avg_profloss, '\n', 
             line_max_profloss, '\n', line_min_profloss]

with open(analysis_path,'w') as text:
    text.writelines(lines)

