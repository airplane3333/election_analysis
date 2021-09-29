import datetime as dt
import csv
import os 
#Assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")

#create filename variable to direct or indirect path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Init total vote counter, winning candidate, wining count, and wining pecentage
total_votes = 0
winning_candidate = " "
winning_count = 0
winning_percentage = 0


#variable to find canidates
candidate_options = [] 

#canidate votes dictionary
candidate_votes = {}

#assign a variable to save the file to a path
with open(file_to_load) as election_data:
    
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
        # add to the total vote count
        total_votes += 1 
        #print the canidate name from each row
        canidate_name = row[2]
        if canidate_name not in candidate_options:
            candidate_options.append(canidate_name)
            #tracking votes for each canidate added to the canidate_options list
            candidate_votes[canidate_name] = 0
        #add votes to that candidate vote count
        candidate_votes[canidate_name] +=1

#get % of votes by each candidate by looping thru the counts
#iterate throught the candidate_votes
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) * 100
    #print(f"{candidate_name}: received {vote_percentage:.2f}% for the vote")
    print(f"{candidate_name}: {vote_percentage:.2f} ({votes:,})\n")

    #get winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then setn count and % to winning variables
        winning_count = votes
        winning_percentage = vote_percentage
        #set the winning candidate to the candidates name
        winning_candidate = candidate_name
#output to terminal for winning summary
winning_candidate_summary = (
    f"--------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.2f}%\n"
    f"--------------------------------------\n")
print(winning_candidate_summary)
#print the total votes
#print(candidate_votes)
#print(total_votes)
#print(candidate_options)


#close the file
election_data.close()

#using the open() funtion with the w mode will write data to the file
with open(file_to_save,"w") as txt_file:
#output of election resutls
    txt_file.write("Counties in the election \n-------------------------------------------\n")
    txt_file.write("Arapahoe \nDenver \nJefferson")
    txt_file.write("The canidates in the election are: " + str(candidate_options) )
    txt_file.write("\nThe total votes cast: " +str(total_votes))


#close the file
txt_file.close()

#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote