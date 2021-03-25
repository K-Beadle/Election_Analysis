# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter and set to zero
total_votes = 0

# Declaring empty list to store candidates when counted
candidate_options = []
# Declaring empty dictionary to store total votes for each candidate when counted
candidate_votes = {}

# Track the winning candidate, vot count, and percentage
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
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate's name, vote count, and percentage votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count, percentage, and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
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
