
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote

line_title = 'Election Results'
line_break = '-------------------------'
print(line_title)
print(line_break)

import os
import csv

csvpath = os.path.join('resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)    # skip header row

    # ====================================================================================================================
    # code to return the total votes

    row_count = len(list(csvreader))
    line_total_votes = f'Total Votes: {row_count}'     # 1 row = 1 ballot/vote, so count of rows is the count of votes
    print(line_total_votes)
    print(line_break)

    # ====================================================================================================================
    # code to return the results by candidate

    #////////// something is wrong with this section of code = everything returns 0's

    candidate1 = "Charles Casper Stockham"
    candidate2 = "Diana DeGette"
    candidate3 = "Raymon Anthony Doane"
    candidate1_counter = 0
    candidate2_counter = 0
    candidate3_counter = 0

    for row in csvreader:
        if row[2] == candidate1:
            candidate1_counter += 1
        elif row[2] == candidate2:
            candidate2_counter += 1
        elif row[2] == candidate3:
            candidate3_counter += 1
        else:
            print("There are more than 3 candidates in the data.")

    candidate1_percentage = round((candidate1_counter / row_count), 3)
    candidate2_percentage = round((candidate2_counter / row_count), 3)
    candidate3_percentage = round((candidate3_counter / row_count), 3)

    line_candidate1 = f'{candidate1}: {candidate1_percentage}% ({candidate1_counter})'
    line_candidate2 = f'{candidate2}: {candidate2_percentage}% ({candidate2_counter})'
    line_candidate3 = f'{candidate3}: {candidate3_percentage}% ({candidate3_counter})'
    print(line_candidate1)
    print(line_candidate2)
    print(line_candidate3)
    print(line_break)

    #\\\\\\\\\\

    # ====================================================================================================================
    # code to return the winning candidate
    
    winning_percentage = min(candidate1_percentage, candidate2_percentage, candidate3_percentage)

    if winning_percentage == candidate1_percentage:
        line_winner = f'Winner: {candidate1}'
        print(line_winner)
    elif winning_percentage == candidate2_percentage:
        line_winner = f'Winner: {candidate2}'
        print(line_winner)
    elif winning_percentage == candidate3_percentage:
        line_winner = f'Winner: {candidate3}'
        print(line_winner)
    else:
        print("error in winner results")
    
    print(line_break)

# ====================================================================================================================
# code to write outputs to text file in analysis folder

analysis_path = os.path.join('analysis','analysis.txt')

lines = [line_title, '\n', line_break, '\n',
             line_total_votes, '\n', line_break, '\n',
             line_candidate1, '\n', line_candidate2, '\n', line_candidate3, '\n', line_break, '\n', 
             line_winner, '\n', line_break]

with open(analysis_path,'w') as text:
    text.writelines(lines)

