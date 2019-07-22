import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(111)

def animate(i):
    pullData = open('S11_part2.csv', 'r').read()
    dataArray = pullData.split('\n')
    frequency = []
    power = []

    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            frequency.append(float(x))
            power.append(float(y))

    # max_amp = max(rho)
    #
    # thetarad = [x * (np.pi/180) for x in thetadeg]
    #
    #
    #
    # normalized_rho = [x - max_amp for x in rho]
    #
    # min_rho = min(normalized_rho)
    #
    # ax1.clear()
    #
    # ax1.set_theta_direction(-1)
    #
    # ax1.set_theta_zero_location("N")
    #
    # plt.title("Radiation Pattern Normalized")
    #
    # plt.polar(thetarad, normalized_rho)

    ax1.clear()

    plt.title("S11 Part 2")

    plt.autoscale(True)

    plt.plot(frequency,power)

ani = animation.FuncAnimation(fig, animate, interval=100)


plt.show()
