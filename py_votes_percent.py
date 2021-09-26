my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
# statement below uses concatination 
#print("I received " + str(percentage_votes)+"% of the total votes.")
# Now using f-strings in print statement
print(f"I received {my_votes / total_votes *100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")
    #printing using f-strings
    print (f"{county} county has {voters} registered voters.")
# using multiple f-strings 

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")

print(message_to_candidate)