#import os and csv
import os
import csv

#define file path and reader
csvpath = os.path.join("Resources", "election_data.csv")
csvreader = csv.reader(csvpath, delimiter=",")

#create lists to store information
candidates = []
votes = []
total_votes = []

election_candidates = []
candidate_votes = []
percent_vote = []

#open file to reead, file has a header
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)

#append reqd data from file to list
        for row in csvreader:
                votes.append(row[0])
                candidates.append(row[2])

#create a unique list of election candidates 
for item in candidates:
        if item not in election_candidates:
                election_candidates.append(item)

# assign number of votes to each candidate         
for x in election_candidates:
        candidate_votes.append(candidates.count(x))

#calculate total votes cast  
        total_votes = sum(candidate_votes)

#calculate maximum votes, and identify the index number, to identify who won
        max_vote = max(candidate_votes)
        winner_index = candidate_votes.index(max_vote) 
        winner = (election_candidates[winner_index])

# calculate percentage of votes for each candidate
for y in candidate_votes:
        percent = round((y/total_votes * 100), 2)
        percent_vote.append(percent)

#print all results
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
for i,(a,b,c) in enumerate(zip(election_candidates, percent_vote,candidate_votes)):
        print("{} : {}% ({})".format(a,b,c))
        
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")
#create text file
f = open("Election_Results.txt", "x")

#write to text file
f.write("Election Results\n")
f.write("----------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("------------------------------")
for i,(a,b,c) in enumerate(zip(election_candidates, percent_vote,candidate_votes)):
       f.write("{} : {}% ({})\n".format(a,b,c))
        
f.write(f"-------------------------\n")
f.write(f"Winner: {winner}\n")
f.write("--------------------------")