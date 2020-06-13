import os
import csv

# path to input csv
poll_data_path = os.path.join("Resources", "election_data.csv")
doc = open("main.txt","w")

# create lists
data_voters = list()
data_candidates = list()

# open input csv and read columns of interest into our lists
with open(poll_data_path, "r", encoding="utf-8") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        voters = row[0]
        county = row[1]
        candidates = row[2]

        data_voters.append(voters)
        data_candidates.append(candidates)

# setup elections results output
print("Election Results")
print("-------------------------")
    
# number of months in data set
total_voters = len(data_voters)
print("Total Votes:", total_voters)
print("-------------------------")

# total and percentage vote for each candidate
candidate_votes = []
from collections import Counter
candidate_votes = (Counter(data_candidates))
[candidate_votes.keys(), candidate_votes.values()]

for key, value in candidate_votes.items():
    print(key,":", "{:.3f}".format((value / total_voters)*100),"%", "(",value,")")

# the winner
max_key = max(candidate_votes, key=candidate_votes.get)
print("-------------------------")
print("Winner:", max_key)
print("-------------------------")

# produce txt file
print("Election Results", file=doc)
print("-------------------------", file=doc)
print("Total Votes:", total_voters, file=doc)
print("-------------------------", file=doc)
for key, value in candidate_votes.items():
    print(key,":", "{:.3f}".format((value / total_voters)*100),"%", "(",value,")", file=doc)
print("-------------------------", file=doc)
print("Winner:", max_key, file=doc)
print("-------------------------", file=doc)
doc.close()