import os
import csv

#Variable Declaration
numMonths = 0
netPL = 0
changePL = []
maxIncrease = ['', 0]
maxDecrease = ['', 0]

#Open CSV File
csvPath = os.path.join('Resources', 'budget_data.csv')
with open (csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    #Skip Headers
    next(csvReader)

    for row in csvReader:
        numMonths += 1
        netPL += int(row[1])
        changePL.append(int(row[1]))
        #Check Max Increase/Decrease
        if int(row[1]) > maxIncrease[1]:
            maxIncrease[0] = row[0]
            maxIncrease[1] = int(row[1])
        elif int(row[1]) < maxDecrease[1]:
            maxDecrease[0] = row[0]
            maxDecrease[1] = int(row[1])

#Print Results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {numMonths}")
print(f"Total: ${netPL}")
print(f"Average Change: ${round(sum(changePL) / len(changePL), 2)}")
print(f"Greatest Increase in Profits: {maxIncrease[0]} (${maxIncrease[1]})")
print(f"Greatest Decrease in Profits: {maxDecrease[0]} (${maxDecrease[1]})")

#Export Results as Text File

outPath = os.path.join('Analysis', 'output.txt')
with open (outPath, 'w') as txtFile:
    txtFile.write("Financial Analysis\n")
    txtFile.write("----------------------------\n")
    txtFile.write(f"Total Months: {numMonths}\n")
    txtFile.write(f"Total: ${netPL}\n")
    txtFile.write(f"Average Change: ${round(sum(changePL) / len(changePL), 2)}\n")
    txtFile.write(f"Greatest Increase in Profits: {maxIncrease[0]} (${maxIncrease[1]})\n")
    txtFile.write(f"Greatest Decrease in Profits: {maxDecrease[0]} (${maxDecrease[1]})")