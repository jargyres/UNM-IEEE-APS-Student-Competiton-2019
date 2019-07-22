import argparse
import numpy as np
import struct

# import

def complexToSingleArray(array):
    # Convert compex array to real array when
    # I and Q are stored one after each other
    # This is done because numpy can only write
    # complex numbers as to a file in certain data types

    realArray = np.real(array)
    imagArray = np.imag(array)

    # Create array double length of input to hold both real and imag values
    output = np.zeros(realArray.size + imagArray.size)

    # Pack  real (I) and imag (Q) values in the correct order
    # By default numpy writes index 0 to an output file first
    output[0::2] = realArray
    output[1::2] = imagArray

    return output

if __name__ == '__main__':

    # Generate command line parser to parse inputs
    cliParser = argparse.ArgumentParser(description='Plots quadrature IQ signals')

    # Get the filename of the input file
    cliParser.add_argument('filename', type=str, help='input filename')

    cliParser.add_argument('freq', type=float, default=3e9)

    cliParser.add_argument('samplerate', type=float, default=10e6)

    args = cliParser.parse_args()


    filename = args.filename

    frequency = args.freq

    samplerate = args.samplerate


    num_seconds = 0.0001

    num_samples = num_seconds * samplerate

    # given frequency in radians

    signal_freq_rad = frequency * 2 * np.pi

    # Generate a vertor 't' which represents time, in units of samples.
    # This starts at t=0, and creates num_samples samples in steps of 1/num_samples
    # t = slice(0,(num_seconds - 1 / samplerate),(1 / samplerate))

    t = np.arange(0,(num_seconds - 1 / samplerate),(1 / samplerate))
    # print(t)

    signal = 0.90 ** (1j * signal_freq_rad * t)
    # newsig = np.real(signal)
    # newsig = np.round(newsig)
    sig_i = np.array(np.round(np.real(signal)))
    sig_i = sig_i * 2048.0
    for i in sig_i:
        if i > 2047:
            i = 2047
        if i < -2048:
            i = -2048

    # sig_len = 2 * len(sig_i)
    #
    # sig_out = np.arange(1, (sig_len - 1), 2)

    sig_q = np.array(np.round(np.imag(signal)))
    sig_q = sig_q * 2048.0

    for j in sig_q:
        if j > 2047:
            j = 2047
        if j < -2048:
            j = -2048

    sig_len = 2 * len(sig_i)

    sig_out = np.zeros(sig_len)

    # for k in range(0,sig_len-1,2):
    #     sig_out[k] = sig_i[k]
    #
    # for l in range(1, sig_len, 2):
    #     sig_out[l] = sig_q[l]

    # output = np.zeros(realArray.size + imagArray.size)

    # Pack  real (I) and imag (Q) values in the correct order
    # By default numpy writes index 0 to an output file first
    sig_out[0::2] = sig_i
    sig_out[1::2] = sig_q

    sig_out = sig_out.astype(np.int16)




    # sig_out = complexToSingleArray(signal).astype(np.int16)

    filename += ".dat"

    # sig_i = round(np.real(signal) * 2048.0)

    with open(filename, 'wb') as f:
        sig_out.tofile(f)


    # print(signal)

    # SAMPLE_RATE = 2e6;
    # NUM_SECONDS = 10;
    # NUM_SAMPLES = NUM_SECONDS * SAMPLE_RATE;
    # SIGNAL_FREQ_RAD = 250e3 * 2 * pi;
    # t = [0: (1 / SAMPLE_RATE): (NUM_SECONDS - 1 / SAMPLE_RATE)];
    # signal = 0.90 * exp(1j * SIGNAL_FREQ_RAD * t);
