#import os module and module for csv files
import os
import csv

#Store file path
csvpath = os.path.join('../Resources/budget_data.csv')


#Opens CSV file to read and access
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Print Header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Skips header in CSV
    next(csvreader)
    
    #Defined variables
    previous = 0
    change = 0
    total = 0
    totalProfit = 0
    changeList = []
    Inc = ["",0]
    Dec = ["",999999]
    
    #Calculate Total Months, Total Profits, Average Change,
    # Greatest Increase and Greatest Decrease
    
    for row in csvreader:
        total = total + 1
        totalProfit = totalProfit + int(row[1])
        change = int(row[1])-previous
        changeList.append(change)
        previous = int(row[1])
        length = len(changeList)-1
        
        if change > Inc[1]:
            Inc[0]= row[0]
            Inc[1]= change
            
        if change < Dec[1]:
            Dec[0]= row[0]
            Dec[1]= change
            
    average = sum(changeList[1:])/length
        
    #Print results to shell
    print(total)
    print(totalProfit)
    print(average)
    print(Inc[0], Inc[1])
    print(Dec[0], Dec[1])

#Export results as .txt file

result = (f"Total Months:{total}\n"
f"Total Profit:${totalProfit}\n"
f"Average Change:${average}\n"
f"Greatest Increase:${Inc[0], Inc[1]}\n"
f"Greatest Decrease:${Dec[0], Dec[1]}")

output_path = os.path.join("/Users/bryanwilson/Desktop/python-challenge/PyBank","Results.txt")

with open(output_path, "w") as txt_file:
    txt_file.write(result)


   
    

