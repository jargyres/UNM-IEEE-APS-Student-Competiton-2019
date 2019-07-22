import numpy as np
import csv


pullData = open('S11_part1.csv', 'r').read()
dataArray = pullData.split('\n')
frequency = []
power = []

for eachLine in dataArray:
    if len(eachLine)>1:
        x,y = eachLine.split(',')
        frequency.append(float(x))
        power.append(float(y))


pullData2 = open('S11_part2.csv', 'r').read()
dataArray2 = pullData2.split('\n')
frequency2 = []
power2 = []

for eachline in dataArray2:
    if len(eachline)>1:
        j,k = eachline.split(',')
        frequency2.append(float(j))
        power2.append(float(k))





npdataArray = np.array(dataArray)

npdataArray2 = np.array(dataArray2)

npfrequency = np.array(frequency)

npfrequency2 = np.array(frequency2)

nppower = np.array(power)

nppower2 = np.array(power2)

# finalarray = []

npfinalarray = np.empty(len(nppower))




#for i in range(len(npfrequency)):
#    npfrequency2[i] = npfrequency[i]


for j in range(len(nppower)):
    # print(nppower2[j] - nppower[j])
    npfinalarray[j] = (nppower[j] - nppower2[j])

npfinalarray = npfinalarray * -1



for k in range(len(nppower)):
    print(npfinalarray[k])




# datawrite = ['{:06.10f}'.format(frequency), '{:06.10f}'.format(pwrdeg)]
#
# with open('S11_part2.csv', 'a') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerow(datawrite)
#
# writeFile.close()

for ii in range(len(npfinalarray)):
    freq = npfrequency2[ii]
    pwr = npfinalarray[ii]
    datawrite = ['{:06.10f}'.format(freq), '{:06.10f}'.format(pwr)]

    with open('finalS11.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(datawrite)

    writeFile.close()

# print(npfinalarray)

# print(npfrequency)
#
# print(npfrequency2)






