import os
import csv

#Variable Declaration
canDict = {}

#Open CSV File
csvPath = os.path.join('Resources', 'election_data.csv')
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    next(csvReader)

    #Iterate through CSV
    for row in csvReader:

        #Add canidate/Increment vote count
        if not (row[2] in canDict.keys()):
            canDict.update({row[2]: 1})
        else:
            canDict[row[2]] += 1

#Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {sum(canDict.values())}")
print("-------------------------")
#Print Each Canidate & Respective %
for key in canDict:
    print(f"{key}: {round((canDict[key] / sum(canDict.values())) * 100, 2)}% ({canDict[key]})")
print("-------------------------")
print(f"Winner: {max(canDict, key=canDict.get)}")
print("-------------------------")

#Export Results to File
outPath = os.path.join('Analysis', 'output.txt')
with open (outPath, 'w') as txtFile:
    txtFile.write("Election Results\n")
    txtFile.write("-------------------------\n")
    txtFile.write(f"Total Votes: {sum(canDict.values())}\n")
    txtFile.write("-------------------------\n")
    #Print Each Canidate & Respective %
    for key in canDict:
        txtFile.write(f"{key}: {round((canDict[key] / sum(canDict.values())) * 100, 2)}% ({canDict[key]})\n")
    txtFile.write("-------------------------\n")
    txtFile.write(f"Winner: {max(canDict, key=canDict.get)}\n")
    txtFile.write("-------------------------\n")