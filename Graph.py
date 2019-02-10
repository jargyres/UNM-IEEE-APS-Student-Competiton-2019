import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import VoltageData


def graph():

    fig = plt.figure()

    ax1 = fig.add_subplot(111, projection = 'polar')

    ax1.set_theta_zero_location('N')

    ax1.set_theta_direction(-1)
    def animate(i):
        # r = open("example1.txt", "r").read()
        #
        # lines = r.split('\n')

        degreePoints = []

        graphPoints = VoltageData.getData()

        # for line in lines:
        #     graphPoints.append(line)

        for j in range(len(graphPoints)):
            degreePoints.append((j/200) * (2*np.pi))

        # if(len(graphPoints) <= 200):
        #
        #
        #     ax1.clear()
        #
        #     if(len(graphPoints) >= 1):
        #
        #
        #         ax1.set_rmax(max(graphPoints))
        #
        #     ax1.plot(degreePoints,graphPoints)
        #
        #     ax1.set_title('Raw Voltage Data')
        #
        #     VoltageData.createData()
        # else:
        #     graphNormalizedData()
        ax1.clear()

        for points in graphPoints:
            if points < 0:
                points *= -1

        if(len(graphPoints) >= 1):


            ax1.set_rmax(max(graphPoints))

        ax1.plot(degreePoints,graphPoints)

        ax1.set_title('Raw Voltage Data')

        VoltageData.createData()



    ani = animation.FuncAnimation(fig, animate, interval = 5)

    plt.show()


def graphNormalizedData():
    fig = plt.figure()

    ax1 = fig.add_subplot(111, projection='polar')

    ax1.set_theta_zero_location('E')

    ax1.set_theta_direction(1)


    VoltageData.normalize()

    graphData = VoltageData.getData()

    degreePoints = []

    for j in range(len(graphData)):
        degreePoints.append((j / 200) * (2 * np.pi))

    ax1.plot(degreePoints, graphData)

    ax1.set_title('Normalized Voltage Data')



    plt.show()



