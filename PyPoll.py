import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variable set to zero for our vote counter
total_votes = 0

# Declaring list to count candidates
candidate_options = []
# Declaring dictionary to count total votes for each candidate
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        # loop through each row for the candidate name
        candidate_name = row[2]

        # If candidate name is not in list then add to list
        if candidate_name not in candidate_options:
            
            # Add candidates name to the list
            candidate_options.append(candidate_name)

            # Begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
            
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1


# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes
    #print(f"{candidate_name}: recieved {vote_percentage:,.1f}% of the total vote count.")

# To do: print out each candidate's name, vote count, and percentage votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
)
print(winning_candidate_summary)

#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print the candidate vote dictionary
#print(candidate_votes)
