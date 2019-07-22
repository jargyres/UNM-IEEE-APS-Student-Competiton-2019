import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
#normalized_rho = np.zeros([36,1])

ax1 = fig.add_subplot(111, polar=True)

ax1.set_theta_zero_location("N")

def animate(i):
    pullData = open('data.csv', 'r').read()
    dataArray = pullData.split('\n')
    thetadeg = []
    rho = []

    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            thetadeg.append(int(x))
            rho.append(float(y))

    

    max_amp = max(rho)

    thetarad = [x * (np.pi/180) for x in thetadeg]



    normalized_rho = [x - max_amp for x in rho]

    min_rho = min(normalized_rho)

    ax1.clear()

    ax1.set_theta_direction(-1)

    ax1.set_theta_zero_location("N")

    plt.title("Radiation Pattern Normalized")

    plt.polar(thetarad, normalized_rho)

    if(thetadeg[(len(thetadeg) - 1)] == 360):
        quit()

ani = animation.FuncAnimation(fig, animate, interval=100)


plt.show()
