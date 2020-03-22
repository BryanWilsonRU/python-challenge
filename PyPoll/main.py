#import os module and module for csv files
import os
import csv

#Store file path
csvpath = os.path.join('/Users/bryanwilson/Desktop/Instructions/PyPoll/Resources/election_data.csv')


#Opens CSV file to read and access
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Print Header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Defined Variable
    totalVotes = 0
    candidate = 0
    
    
    for row in csvreader:
        totalVotes = totalVotes + 1

    print(totalVotes)
        
    #Skip header row
    #next(csvreader)

    
  
   
result = (f"Total Votes:{totalVotes}")

output_path = os.path.join("/Users/bryanwilson/Desktop/python-challenge/PyPoll","Results.txt")

with open(output_path, "w") as txt_file:
    txt_file.write(result)
