import random
import matplotlib.pyplot as plt
import numpy as np
import RadixSort
randnums = []
graphingnums = []
theta = []

for i in range(200):
    randnums.append(random.randint(1,5))



for j in range(randnums.__len__()):
    graphingnums.append("%s%s" %(randnums[j - 1], randnums[j]))

#pass graphingnums as a integer for graphing
for k in range(graphingnums.__len__()):
    graphingnums[k] = int(graphingnums[k])


#create the angles for graphing
for i in range(200):
    theta.append(i * 1.8)



#normalize the fuction
for i in range(graphingnums.__len__()):
    graphingnums[i] = (graphingnums[i]/max(graphingnums))

# for i in range(len(graphingnums)):
#     arr = RadixSort.radixSort(graphingnums)
#     graphingnums[i] = arr[i]



print("randnums = %s" % randnums)
print("randnums length = %s" % randnums.__len__())
print("graphingnums = %s" % graphingnums)
print("graphingnums length = %s" % graphingnums.__len__())
print("theta = %s" % theta)


ax = plt.subplot(111, projection='polar')
ax.plot(theta,graphingnums)
# ax.scatter(theta,graphingnums)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
# ax.set_rmax(average/ max(graphingnums))
plt.show()