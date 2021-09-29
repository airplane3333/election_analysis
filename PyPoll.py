import datetime as dt
import csv
import os 
#Assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")

#create filename variable to direct or indirect path
file_to_save = os.path.join("analysis","election_analysis.txt")
#assign a variable to save the file to a path
with open(file_to_load) as election_data:
    #to do:read and analyze data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print (headers)
    #print each row in the csv file
    #for row in file_reader:
     #   print(row)
  


#open the election resutls
#election_data = open(file_to_load,"r")
#perform analysis


#close the file
election_data.close()


#

#using the open() funtion with the w mode will write data to the file
with open(file_to_save,"w") as txt_file:
#output of election resutls
    txt_file.write("Counties in the election \n-------------------------------------------\n")
    txt_file.write("Arapahoe \nDenver \nJefferson")


#close the file
txt_file.close()

#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote