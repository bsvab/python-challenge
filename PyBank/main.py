import os
import csv

# this comment is typical for all "line_descriptor" variables in the following code:
    # purpose is to save all lines to be eventually printed to the .txt file as variables so I can use them to print to terminal and to .txt without typing it out twice

line_title = 'Financial Analysis'   
line_break = '----------------------------'
print(line_title)
print(line_break)

csvpath = os.path.join('resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)             # skip header row

    # return the total months, return the total profit/loss, and generate lists of the dates and profit/loss change values...

    total_profloss = 0          # establishing total profit/loss amount accumulator
    row_count = 0               # establishing row (month) count accumulator
    profloss_change = 0         # establishing variable for the profit/loss deltas to be populated into a dict in the for loop
    list_profloss_change = []   # establishing empty list to pull all the profit/loss change values into in order to feed into sum/min/max formulas later 
    list_dates = []             # establishing empty list to pull all the date strings into in order to feed into min/max printout later 

    for row in csvreader:
        dates = row[0]
        if row_count >= 1:                                      # conditional needed to skip the first value since there is nothing to calculate a delta from
            profloss_change = int(row[1])-profloss              # calc profloss_change and apply to variable
            list_profloss_change.append(profloss_change)        # populate list
            list_dates.append(dates)                            # populate list
        profloss = int(row[1])                                  # apply profloss value to variable
        total_profloss += profloss                              # increase accumulator for total_profloss
        row_count += 1                                          # increase accumulator for row (month) count
    
    line_total_months = f'Total Months: {row_count}'            # 1 row = 1 month, so count of rows is the count of months
    print(line_total_months)
    line_total_profloss = f'Total: ${total_profloss}'
    print(line_total_profloss)

    # return the average change...

    avg_profloss_change = round((sum(list_profloss_change) / (row_count - 1)),2)   # calc average profit/loss change
    
    line_avg_profloss_change = f'Average Change: ${avg_profloss_change}'
    print(line_avg_profloss_change)

    # return the greatest increase and greatest decrease in profits + associated dates

    min_profloss = min(list_profloss_change)                            # identify min change
    min_profloss_index = list_profloss_change.index(min_profloss)       # identify min change index so can use to cross-reference same index in dates list
    min_profloss_date = list_dates[min_profloss_index]                  # pull date corresponding to same index as min change value

    max_profloss = max(list_profloss_change)                            # identify max change
    max_profloss_index = list_profloss_change.index(max_profloss)       # identify max change index so can use to cross-reference same index in dates list
    max_profloss_date = list_dates[max_profloss_index]                  # pull date corresponding to same index as max change value

    line_max_profloss = f'Greatest Increase in Profits: {max_profloss_date} (${max_profloss})'
    print(line_max_profloss)
    line_min_profloss = f'Greatest Decrease in Profits: {min_profloss_date} (${min_profloss})'
    print(line_min_profloss)

# write outputs to text file in analysis folder...

analysis_path = os.path.join('analysis','analysis.txt')

lines = [line_title, '\n', line_break, '\n',
             line_total_months, '\n', line_total_profloss, '\n', line_avg_profloss_change, '\n', 
             line_max_profloss, '\n', line_min_profloss]

with open(analysis_path,'w') as text:
    text.writelines(lines)

