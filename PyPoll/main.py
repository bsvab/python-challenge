import os
import csv

# this comment is typical for all "line_descriptor" variables in the following code:
    # purpose is to save all lines to be eventually printed to the .txt file as variables so I can use them to print to terminal and to .txt without typing it out twice

line_title = 'Election Results'
line_break = '-------------------------'
print(line_title)
print(line_break)

csvpath = os.path.join('resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)     # skip header row

    # return the total votes and results by candidate...

    candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]                   # establishing list of all candidate names
    votes = [1 if vote[2] == candidates[0] else 2 if vote[2] == candidates[1] else \
             3 if vote[2] == candidates[2] else 'error' for vote in csvreader]                          # list comprehension w/ conditionals to assign 1/2/3 identifiers to ea candidate's votes and feed into list to be processed later; also captures errors if there were names in data other than the candidate list
    
    total_votes = len(votes)                                                                            # total votes identified via length of list established in line above
    candidate_votes = [votes.count(1), votes.count(2), votes.count(3)]                                  # make list of ea candidate's vote count using .count w/ 1/2/3 identifier
    if votes.count('error') > 0:
        print('vote counter error: data displayed is missing candidates')                               # this isn't really needed given the data set received, but figured I'd practice adding in an error-checker
    candidate_vote_percentages = [round(count / total_votes * 100, 3) for count in candidate_votes]     # calculates percent of total vote by candidate and feeds into list
    
    line_total_votes = f'Total Votes: {total_votes}'
    print(line_total_votes)
    print(line_break)
    
    line_candidate1 = f'{candidates[0]}: {candidate_vote_percentages[0]}% ({candidate_votes[0]})'
    line_candidate2 = f'{candidates[1]}: {candidate_vote_percentages[1]}% ({candidate_votes[1]})'
    line_candidate3 = f'{candidates[2]}: {candidate_vote_percentages[2]}% ({candidate_votes[2]})'
    print(line_candidate1)
    print(line_candidate2)
    print(line_candidate3)
    print(line_break)

    # return the winning candidate...
    
    winning_percentage = max(candidate_vote_percentages)                         # winning percentage identified via finding the max value in the of list of candidate vote percentages
    winner = candidates[candidate_vote_percentages.index(winning_percentage)]    # winner is pulled from candidates list by using the index of the winning percentage value in the percentages list

    line_winner = f'Winner: {winner}'
    print(line_winner)
    print(line_break)

# write outputs to text file in analysis folder...

analysis_path = os.path.join('analysis','analysis.txt')

lines = [line_title, '\n', line_break, '\n',
             line_total_votes, '\n', line_break, '\n',
             line_candidate1, '\n', line_candidate2, '\n', line_candidate3, '\n', line_break, '\n', 
             line_winner, '\n', line_break]

with open(analysis_path,'w') as text:
    text.writelines(lines)