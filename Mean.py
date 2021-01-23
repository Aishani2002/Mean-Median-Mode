import csv

with open("Data.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    nNum= fileData[i][1]
    newData.append(float(nNum))
    
n=len(newData)
total = 0
for r in newData:
    total += r
    
mean= total/n
print("mean: %f" % mean)