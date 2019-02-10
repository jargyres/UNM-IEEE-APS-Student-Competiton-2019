import time
import random
def normalization(data):


    for i in range(len(data)):

        data[i] /= max(data)

    return data



def getData():


    voltage_data = open("exp.txt", "r+").read()

    data_points = []

    dataCounter = 0

    for line in voltage_data.split('\n'):
        if dataCounter <= 200:

            if(len(line) == 0):
                data_points.append(0)
                dataCounter+=1
            else:
                data_points.append(float(line))
                dataCounter+=1


    return data_points

def printData(data):

    for i in range(len(data)):

        print(data[i])


def write_normalize_data(normalized_data_arr):
    write_data = open("example1.txt", "w+")

    for i in range(len(normalized_data_arr)):

        write_data.write("%s\n" % (normalized_data_arr[i]))



def normalize():
    write_normalize_data(normalization(getData()))


def createData():
    write_data = open("example1.txt", "a")
    write_data.write("%s\n" % random.randint(1,5))
    write_data.close()




def autoData():
    for i in range(5):
        createData()
        time.sleep(0.01)




