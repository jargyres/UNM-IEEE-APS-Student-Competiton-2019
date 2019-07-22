import argparse
import numpy as np
import matplotlib.pyplot as plt
import csv
import struct

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

    cliParser.add_argument('Horizontal_deg', type=int, default=0)

    cliParser.add_argument('Vertical_deg', type=int, default=0)

    cliParser.add_argument('freq', type=float, default=3e9)

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

    if args.offset != 0:

        fileOffset = args.offset

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

    NUM_SAMPLES = 2000

    timestep = 1 / NUM_SAMPLES

    bin2csv(binfile=args.filename, csvfile='csvfile.csv')

    f = open('csvfile.csv', 'r')

    dataI = []

    dataQ = []

    n = 0

    sumI = 0

    sumQ = 0

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

        I = dataI[i]/2048.0
        Q = dataQ[i]/2048.0
        dataI[i] = I
        dataQ[i] = Q
        dataC.append(complex(I, Q))  # this one has complex data



    horizontal_deg = args.Horizontal_deg

    vertical_deg = args.Vertical_deg

    freq=args.freq







    f = np.linspace(-0.5 * SAMPLE_RATE, 0.5 * SAMPLE_RATE, len(dataC))
    f_carrier = np.linspace(-0.5 * SAMPLE_RATE, 0.5 * SAMPLE_RATE, len(dataC)) + (freq - 5e6)
    data_fft = (20 * np.log10(np.abs(np.fft.fftshift(np.fft.fft(dataC))) / NUM_SAMPLES)) - 20
    carrier_data = [np.transpose(f_carrier), data_fft]



    carrier_data = np.array(carrier_data)


    indexes = indices(carrier_data[0], lambda x: x > freq - 1e6 and x < freq + 1e6)

    pwrdeg=max(data_fft[indexes])

    print(pwrdeg)

    datawrite = ['{:d}'.format(horizontal_deg), '{:d}'.format(vertical_deg), '{:06.10f}'.format(pwrdeg)]

    datawrite2D = ['{:d}'.format(horizontal_deg), '{:06.10f}'.format(pwrdeg)]

    with open('data3D.csv', 'a') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerow(datawrite)


    writeFile.close()


    with open('data.csv', 'a') as writefile:

        writ = csv.writer(writefile)

        writ.writerow(datawrite2D)


    writefile.close()
