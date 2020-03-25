#import os module and module for csv files
import os
import csv

#Store file path
csvpath = os.path.join('../Resources/election_data.csv')


#Opens CSV file to read and access
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Print Header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Defined Variable
    totalVotes = 0
    candidateList = []
    candidateCount = {}
    candidatePct = {}
    
    for row in csvreader:
        totalVotes = totalVotes + 1
        
        if row[2] not in candidateList:
            candidateList.append(row[2])
        
            candidateCount[row[2]] = 0
        candidateCount[row[2]] = candidateCount[row[2]] + 1
        
    for x in candidateCount:
       candidatePct[x] = (round(candidateCount[x]/totalVotes*100,2))
       
    winner = list(candidatePct.keys())[list(candidatePct.values()).index(max(candidatePct.values()))]
    
    print("Election Results")
    print("Total Votes: " + str(totalVotes))
    print("Candidate List: " + str(candidateCount))
    print("Vote Percentage: " + str(candidatePct) + "%")
    print("Winner: " + winner)
    
  
   
result = (f"Election Results\n"
f"Total Votes:{totalVotes}\n"
f"Candidate List: {candidateCount}\n"
f"Vote Percentage: {candidatePct}%\n"
f"Winner: {winner}")


with open(output_path, "w") as txt_file:
    txt_file.write(result)
