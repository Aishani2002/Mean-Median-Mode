import csv
from collections import Counter

with open("Data.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    nNum= fileData[i][1]
    newData.append(nNum)
    
data = Counter(newData)
modeDataforRange = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurance in data.items():
    if 50<float(height)<60:
        modeDataforRange["50-60"]+=occurance
    elif 60<float(height)<70:
        modeDataforRange["60-70"]+=occurance
    elif 70<float(height)<80:
        modeDataforRange["70-80"]+=occurance

modeRange, modeOccurence= 0,0
for range,occurance in modeDataforRange.items():
    if occurance>modeOccurence:
        modeRange, modeOccurence=[int(range.split("-")[0]),int(range.split("-")[1])], occurance

mode= float((modeRange[0]+modeRange[1])/2)
print("mode: ", mode)     