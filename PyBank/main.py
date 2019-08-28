import os
import csv

nmonths = 0
totalchange = 0
maxinc = 0
maxincdate = ""
maxdec = 0
maxdeccdate = ""
    
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 
    
    for row in csvreader:
        if nmonths == 0:
            maxinc = float(row[1])
            maxdec = float(row[1])
            maxincdate = row[0]
            maxdecdate = row[0]
        else:
            if float(row[1]) > maxinc:
                maxinc = float(row[1])
                maxincdate = row[0]
            elif float(row[1]) < maxdec:
                maxdec = float(row[1])
                maxdecdate = row[0]
        nmonths += 1
        totalchange += float(row[1])

avgchange = totalchange / nmonths

results = []
results.append("Financial Analysis\n----------------------------")
results.append(f"Total Months: {nmonths}")
results.append(f"Total: ${round(totalchange)}")
results.append(f"Average Change: ${round(avgchange,2)}")
results.append(f"Greatest Increase in Profits: {maxincdate} (${round(maxinc)})")
results.append(f"Greatest Decrease in Profits: {maxdecdate} (${round(maxdec)})")

filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')
