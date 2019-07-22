import matplotlib.pyplot as plt


fig = plt.figure()

pullData = open('finalS11.csv', 'r').read()
dataArray = pullData.split('\n')
frequency = []
power = []

for eachLine in dataArray:
    if len(eachLine)>1:
        x,y = eachLine.split(',')
        frequency.append(float(x))
        power.append(float(y))

plt.title("S11 Final Plot")

plt.autoscale(True)

plt.plot(frequency,power)

plt.show()
