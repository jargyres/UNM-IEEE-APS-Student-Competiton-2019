import numpy as np
import csv


pullData = open('data3D.csv', 'r').read()
dataArray = pullData.split('\n')
theta = []
phi = []
power = []

for eachLine in dataArray:
    if len(eachLine)>1:
        x,y,z = eachLine.split(',')
        theta.append(int(x))
        phi.append(int(y))
        power.append(float(z))

i = 36



while i <= len(power):
	power[i] = power[i-36]
	i = i + 37


for ii in range(len(power)):
    THETA = theta[ii]
    PHI = phi[ii]
    POWER = power[ii]
    datawrite = ['{:d}'.format(THETA), '{:d}'.format(PHI), '{:06.10f}'.format(POWER)]

    with open('final3Ddata.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(datawrite)

    writeFile.close()







