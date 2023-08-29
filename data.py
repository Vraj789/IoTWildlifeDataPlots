import matplotlib.pyplot as plt
import re 
import numpy as np
import math

title = "";
X, Y = [], []
count = 0;

#oxygen-time graph
for line in open('HealthyData.txt', 'r'):
    if count < 2:
        if "Zebra" in line:
            title = "Zebra"
            count=count+1
            print(count)
        if "Elephant" in line:
            title = "Elephant"
    
        if "Timestamp" in line:
            result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            #print(result[0])
            X.append(float(result[0]))
        if "oxygen_saturation" in line:
            ans = line.split(',', 1)[0]
            result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
            #print(result[0])
            Y.append(float(result[0]))
    # values = [float(s) for s in line.split()]
    # Y.append(values[1])
plt.xlabel("Timestamp")
plt.ylabel("Oxygen Saturation")
plt.title(title)
plt.plot(X, Y)
plt.show()

X, Y = [], []
count = 0;

for line in open('HealthyData.txt', 'r'):
    if count < 2:
        if "Zebra" in line:
            title = "Zebra"
            count=count+1
            print(count)
        if "Elephant" in line:
            title = "Elephant"
    
        if "Timestamp" in line:
            result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            #print(result[0])
            X.append(float(result[0]))
        if "heart_rate" in line:
            ans = line.split(',', 1)[1]
            result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
            #print(result[0])
            Y.append(float(result[0]))
    # values = [float(s) for s in line.split()]
    # Y.append(values[1])
plt.xlabel("Timestamp")
plt.ylabel("Heart Rate")
plt.title(title)
plt.plot(X, Y)
plt.show()

#X location-time graph
X, Y = [], []
for line in open('HealthyData.txt', 'r'):
    if "Zebra" in line:
        title = "Zebra"
    if "Elephant" in line:
        title = "Elephant"
    if "Timestamp" in line:
        result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        print(result[0])
        X.append(float(result[0]))
    if "location" in line:
        ans = line.split(',', 1)[0]
        result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
        print(result[0])
        Y.append(float(result[0]))

    # values = [float(s) for s in line.split()]
    # Y.append(values[1])
plt.xlabel("Timestamp")
plt.title(title)
plt.ylabel("X Direction Movement")
plt.plot(X, Y)
plt.show()

#Y location-time graph
X, Y = [], []

for line in open('HealthyData.txt', 'r'):
    if "Zebra" in line:
        title = "Zebra"
    if "Elephant" in line:
        title = "Elephant"
    if "Timestamp" in line:
        result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
        print(result[0])
        X.append(float(result[0]))
    if "location" in line:
        ans = line.split(',', 1)[1]
        result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
        print(result[0])
        Y.append(float(result[0]))

    # values = [float(s) for s in line.split()]
    # Y.append(values[1])
plt.xlabel("Timestamp")
plt.ylabel("Y Direction Movement")
plt.title(title)
plt.plot(X, Y)
plt.show()

#x-y location graph
X, Y = [], []

for line in open('HealthyData.txt', 'r'):
    if "Zebra" in line:
        title = "Zebra"
    if "Elephant" in line:
        title = "Elephant"
    
    if "location" in line:
        ans = line.split(',', 1)[0]
        result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
        print(result[0])
        X.append(float(result[0]))
    if "location" in line:
        ans = line.split(',', 1)[1]
        result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
        print(result[0])
        Y.append(float(result[0]))
    # values = [float(s) for s in line.split()]
    # Y.append(values[1])
plt.xlabel("X Direction Movement")
plt.ylabel("Y Direction Movement")
plt.title(title)
plt.plot(X, Y)
plt.show()

title = "";
X, Y, time, dists, speeds = [], [], [], [], []
count = 0;


for line in open('SpeedData.txt', 'r'):
    if count < 2:
        if "Zebra" in line:
            title = "Zebra"
            count=count+1
            print(count)
        if "Elephant" in line:
            title = "Elephant"
    
        if "Timestamp" in line:
            result = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            #print(result[0])
            time.append(float(result[0]))
        if "location" in line:
            ans = line.split(',', 1)[0]
            result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
            #print(result[0])
            X.append(float(result[0]))
        if "location" in line:
            ans = line.split(',', 1)[1]
            result = re.findall(r"[-+]?\d*\.\d+|\d+", ans)
            Y.append(float(result[0]))

#distance formula calculations
size = len(X)
total = 0
for x in range(0, size-2):
    xDist = X[x+1] - X[x]
    yDist = Y[x+1] - Y[x]
    xDist = xDist**2
    yDist = yDist**2
    total = math.sqrt(xDist + yDist)
    dists.append(total)
    print(xDist)
    print (yDist)

size = len(dists)
for x in range(0, size):
    speeds.append(dists[x]/time[x])

#cdf calculations
sortSpeed = np.sort(speeds)
y = 1. * np.arange(len(speeds)) / (len(speeds) - 1)

#plot CDF
plt.plot(sortSpeed, y)
plt.xlabel('Speeds')
plt.show()   

   
   



