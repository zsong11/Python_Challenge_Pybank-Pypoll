import csv
import os

input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "1_Analysis.txt")

total_vote_count = 0
list_of_candidate = []
vote_count_by_candidate = {}

vote_winner = 0

with open(input_file) as data:
    table = csv.reader(data)
    header = next(table)
    
    for row in table:
        total_vote_count += 1
        name = row[2]

        if name not in list_of_candidate:
            list_of_candidate.append(name)
            vote_count_by_candidate[name] = 0
        
        vote_count_by_candidate[name] += 1

result_1 = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote_count}\n"
        f"-------------------------\n")
print(result_1)

with open(output_file, "w") as txt_file:
    txt_file.write(result_1)

    for name in vote_count_by_candidate:
        vote_indi = vote_count_by_candidate.get(name)
        vote_percentage = (float(vote_indi) / float(total_vote_count)) * 100

        if vote_indi > vote_winner:
            vote_winner = vote_indi
            winner = name

        result_2 = f"{name}: {vote_percentage:.3f}% ({vote_indi})\n"
        print(result_2, end="")

        txt_file.write(result_2)

    result_3 = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(result_3)

    txt_file.write(result_3)