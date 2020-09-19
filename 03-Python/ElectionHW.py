import csv
import os

#Files to load
inputFile = os.path.join(r"PyPoll\\Resources", r"election_data.csv")

#Total Vote Counter
total_votes = 0

#Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

#Reading CSV and converting to a list of dictionaries
with open(inputFile) as election_data:
    reader = csv.reader(election_data)

    #Reading the header
    header = next(reader)

    #For each row
    for row in reader:

        #Running the loader animation
        print(". ", end=""),

        #Adding to the total vote count
        total_votes = total_votes + 1

        #Extracting candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            #Adding to list of candidates running
            candidate_options.append(candidate_name)

            #Tracking candidate's voter count
            candidate_votes[candidate_name] = 0

        #Adding votes to candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Printing results and exporting to a .txt file
outputFile = os.path.join(r"PyPoll\\Resources", r"output.txt")
with open(outputFile, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)