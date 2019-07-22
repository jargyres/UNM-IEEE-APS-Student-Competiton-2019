import argparse
# from sys import byteorder
import numpy as np
import matplotlib.pyplot as plt
import csv
import struct
# import sys
# from pathlib import Path
# from array import array
#
# from rtlsdr import RtlSdr
#
# import ctypes




#
#
def chunked_read(fobj, chunk_bytes=4 * 1024):
    while True:
        data = fobj.read(chunk_bytes)
        if (not data):
            break
        else:
            yield data
#
#
def bin2csv(binfile=None, csvfile=None, chunk_bytes=4 * 1024):
    with open(binfile, 'rb') as b:
        with open(csvfile, 'w') as c:
            csvwriter = csv.writer(c, delimiter=',')
            count = 0
            for data in chunked_read(b, chunk_bytes=chunk_bytes):
                count += len(data)
                for i in range(0, len(data), 4):
                    sig_i, = struct.unpack('<h', data[i:i + 2])
                    sig_q, = struct.unpack('<h', data[i + 2:i + 4])
                    csvwriter.writerow([sig_i, sig_q])
    #print("Processed", str(count // 2 // 2), "samples.")
    # result = np.array(list(csv.reader(open(csvfile, "r"), delimiter=","))).astype("float")
    # return result
#
# def bin2matrix(binfile):
#     f = open(binfile, 'r')
#     # print(f)
#     # print("fsample = ", fsample)
#
#     dataI = []
#     dataQ = []
#
#     n = 0
#     sumI = 0
#     sumQ = 0
#     # read I, Q - values into memory
#     for line in f:
#         list = line.split(',')  # two values with comma inbetween
#         Q = int(list[0])
#         I = int(list[1])
#         # print 1st 10 lines of data-file
#         if n == 0:
#             print
#             '1st 10 lines of I/Q-values'
#         if n < 10:
#             print
#             I, Q
#         dataI.append(I)  # save data in memory
#         dataQ.append(Q)
#         sumI += I
#         sumQ += Q
#         n += 1
#
#     averI = sumI / n  # calculate average
#     averQ = sumQ / n

    # averI = 0 # debug
    # averQ = 0 # debug

#   print
#    "n = ", n
# def load_bin(filename=None):
#
#     f = open(filename, 'r')
#
#     data = f.read(f)
#
#     signal_i = data(slice[1:2:data[-1] - 1], slice[:])/ 2048.0
#
#     signal_q = data(slice[2:2:data[-1]], slice[:]) / 2048.0
#
#     signal = (signal_i + 1) * signal_q;
#
#
#     f.close()




def plotPSD(data, fftWindow, Fs):
    assert fftWindow in ['rectangular', 'bartlett', 'blackman',
                         'hamming', 'hanning']

    N = len(data)

    # Generate the selected window
    if fftWindow == "rectangular":
        window = np.ones(N)
    elif fftWindow == "bartlett":
        window = np.bartlett(N)
    elif args.fftWindow == "blackman":
        window = np.blackman(N)
    elif fftWindow == "hamming":
        window = np.hamming(N)
    elif fftWindow == "hanning":
        window = np.hanning(N)

    dft = np.fft.fft(data * window)

    if Fs == None:
        # If the sample rate is known then plot PSD as
        # Power/Freq in (dB/Hz)
        plt.psd(data * window, NFFT=N)
        print("first")
    else:
        # If sample rate is not known then plot PSD as
        # Power/Freq as (dB/rad/sample)
        plt.psd(data * window, NFFT=N, Fs=Fs)
        print("second")
    plt.show()


def indices(a, func):
    return [i for (i, val) in enumerate(a) if func(val)]


if __name__ == '__main__':

    # Generate command line parser to parse inputs
    cliParser = argparse.ArgumentParser(description='Plots quadrature IQ signals')

    # Get the filename of the input file
    cliParser.add_argument('filename', type=str, help='input filename')

    cliParser.add_argument('deg', type=int, default=0)

    cliParser.add_argument('freq', type=float, default=3e9)

    # cliParser.add_argument('offset', type=float, default=0)

    cliParser.add_argument('-s', '--startSample', type=int,
                           help='sample to begin plot from (default=0)', default=0)

    cliParser.add_argument('-o', '--offset', type=int,
                           help='offset in bytes from begining of file (default=0)', default=0)

    cliParser.add_argument('-n', '--numberOfSamples', type=int,
                           help='number of samples to plot', default=0)

    cliParser.add_argument('-fs', '--sampleRate', type=float,
                           help='sets the sample rate [sps] (default=1e6)')

    cliParser.add_argument('-f', '--format', type=str,
                           help='Output format (default=int16)',
                           choices=["int8", "int16", "int32", "uint8", "uint16", "uint32",
                                    "float16", "float32", "float64"],
                           default='int16')

    cliParser.add_argument('-be', '--bigendian', action='store_true',
                           help='output data in big endian format (default=False)')

    cliParser.add_argument('-qi', '--orderQI', action='store_true',
                           help='store output data as Q then I (Default = I then Q)')

    cliParser.add_argument('-p', '--plotType', type=str,
                           help='Plot Type (default=iq)', choices=['iq', 'psd', 'spec'],
                           default='iq')

    cliParser.add_argument('-w', '--fftWindow', type=str,
                           help='FFT window type (default=rectangular)',
                           choices=['rectangular', 'bartlett', 'blackman', 'hamming', 'hanning'],
                           default='rectangular')

    cliParser.add_argument('-fw', '--fftWidth', type=int,
                           help='FFT width for spectrogram')

    args = cliParser.parse_args()

    # By default the file is read from an offset of 0 bytes
    fileOffset = 0

    # Set initial offset in bytes
    # Useful if the file has a header that should be ignored
    if args.offset != 0:
        fileOffset = args.offset

    # Convert sample offset to offset in bytes depending on datatype
    if args.startSample != 0:
        if args.format[-1:] == "8":
            fileOffset += 2 * 1 * args.startSample
        elif args.format[-2:] == "16":
            fileOffset += 2 * 2 * args.startSample
        elif args.format[-2:] == "32":
            fileOffset += 2 * 4 * args.startSample
        elif args.format[-2:] == "64":
            fileOffset += 2 * 8 * args.startSample






    SAMPLE_RATE = 20e6

    NUM_SAMPLES = 5000

    timestep = 1 / NUM_SAMPLES

    bin2csv(binfile=args.filename, csvfile='csvfile.csv')

    f = open('csvfile.csv', 'r')

    dataI = []

    dataQ = []

    n = 0

    sumI = 0

    sumQ = 0

    # read I, Q - values into memory
    for line in f:
        list = line.split(',')  # two values with comma inbetween
        Q = int(list[1])
        I = int(list[0])
        # print 1st 10 lines of data-file
        dataI.append(I)  # save data in memory
        dataQ.append(Q)
        sumI += I
        sumQ += Q
        n += 1

    averI = sumI / n  # calculate average
    averQ = sumQ / n


    dataC = []
    for i in range(n):
        # I = (dataI[i] - averI)/2048
        # Q = dataQ[i] - averQ
        I = dataI[i]/2048.0
        Q = dataQ[i]/2048.0
        dataI[i] = I
        dataQ[i] = Q
        dataC.append(complex(I, Q))  # this one has complex data



    deg = args.deg

    freq=args.freq

    # offset = args.offset







    f = np.linspace(-0.5 * SAMPLE_RATE, 0.5 * SAMPLE_RATE, len(dataC))
    f_carrier = np.linspace(-0.5 * SAMPLE_RATE, 0.5 * SAMPLE_RATE, len(dataC)) + (freq - 5e6)
    data_fft = (20 * np.log10(np.abs(np.fft.fftshift(np.fft.fft(dataC))) / NUM_SAMPLES)) - 20
    carrier_data = [np.transpose(f_carrier), data_fft]

    # for val in f_carrier:
    #     print(val)
    # print("Using center frequency at")
    # print(freq - 8e6)
    #plots at carrier frequency
    # plt.figure(1)
    #
    # plt.plot(f_carrier, data_fft)
    #
    # plt.xlabel("Frequency (Hz)")
    #
    # plt.ylabel("Power (dB)")
    #
    # plt.title("2,4 GHz Carrier")

    carrier_data = np.array(carrier_data)

    # indexes = np.where(carrier_data[1]>3.0045e9)[0][0]
    #

    #
    # print(data_fft[indexes])

    # print(indexes)
    # print(carrier_data[1])
    # for i in range(len(carrier_data[1])):
    #     print(carrier_data[1][i])
    # maxpowerindex = np.where(carrier_data[1] == carrier_data[1].max())[0][0]
    # index = indices(carrier_data[0], lambda x: x > 3.1995e9 and x < 3.2005e9)

    # print(index)
    indexes = indices(carrier_data[0], lambda x: x > freq - 1e6 and x < freq + 1e6)
    # indexes = indices(carrier_data[0], lambda x: x > 3.0045e9 and x < 3.006e9)

    # print(carrier_data[0])
    # index = np.where(carrier_data[0] > 3.0045e9)
    # print(index)
    # print(maxpowerindex)
    # maxpower = carrier_data.item(maxpowerindex)
    # print(maxpower)
    # powerdeg = max(data_fft[index])
    # print(powerdeg)


    # print(indexes)




    pwrdeg=max(data_fft[indexes])



    index = 0
    for j in range(len(carrier_data[1])):
        if (carrier_data[1][j] == pwrdeg):
            index = j



    frequency = carrier_data[0][index]


    # print("Frequency = ")
    # print(frequency)
    # print("power at that frequency is = ")
    # print(pwrdeg)

    # print(carrier_data[0][index])

    # print(frequencyOfMaxPower)
    # newindexes = data_fft[indexes]

    # print(newindexes)
    # index = np.where(data_fft[indexes] == pwrdeg)
    # print(index)


    # print(index)
    # print("carrier_data[0][index] = ")
    #
    # print(carrier_data[0][index])
    # print("data_fft[index] = ")
    # print(newindexes[index])
    # print("data_fft[0] = ")
    # print(data_fft[0])
    # print(data_fft[index])
    datawrite = ['{:06.10f}'.format(frequency), '{:06.10f}'.format(pwrdeg)]

    # print(datawrite)
    # datatowrite = '{:d},{:06.10f}'.format(deg,powerdeg)

    with open('S11_part1.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(datawrite)


    writeFile.close()
