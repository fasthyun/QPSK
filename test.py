#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:47:30 2026

@author: hyun
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Define the number of points (M=8 for 8-PSK)
M = 8

# 2. Generate the phase angles (0 to 2*pi)
# Points are typically ej(2*pi*n/M)
n = np.arange(M)
phases = (2 * np.pi * n / M +  np.pi/M )

# 3. Calculate complex coordinates (In-phase and Quadrature)
# Constellation points reside on the unit circle
constellation = np.exp(1j * phases)

if False:    
    # 4. Visualization
    plt.figure(figsize=(2, 2))
    plt.scatter(constellation.real, constellation.imag, color='red', marker='o')
    
    # Add unit circle for reference
    circle = plt.Circle((0, 0), 1, color='blue', fill=False, linestyle='--', alpha=0.3)
    plt.gca().add_artist(circle)
    
    # Label points with their index or bit pattern
    for i, point in enumerate(constellation):
        print(i,point)
        plt.text(point.real + 0.05, point.imag + 0.05, f's{i}')

    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.title("8-PSK Constellation Diagram")
    #plt.xlabel("In-phase (I)")
    #plt.ylabel("Quadrature (Q)")
    #plt.grid(True)
    #plt.axis('equal')
    #plt.hide()

from bitstring import BitArray

#BitArray("0o66002674270315476271")
a=BitArray('0x0d805bc5c3367cb9')

#0x0d805bc5c3367cb9
[13, 128, 91, 197, 195, 54, 124, 185]

plt.rcParams['figure.dpi']=80
samp_rate=8000
samps=np.fromfile("/home/hyun/psk8_8k_16t.pcm",dtype='>i2')
#plt.plot(samps[60:200])


from SECLAB_signal import waveview_periodgram, plot_power, plot_time
#samps=samps[0:600] 
#samps.tofile("/home/hyun/psk8_8k_16t_1200.pcm")

#samps=np.fromfile("/home/hyun/psk8_8k_16t.pcm",dtype='>i2')
samps=np.fromfile("/home/hyun/works/QPSK/test_u2_4.pcm",dtype='>i2') # big-endian
#samps=samps[0:600] 
samps=samps[0:]/32000. 
print("len(samps)=",len(samps))
plot_time(samps,'time: ')
plt.show()
    
f,pxx=waveview_periodgram(samps,samp_rate,1024,True)
plot_power(f,pxx,'power(periodgram): ')

#correlate
#plt.plot(k[200:400])
#samps=np.fromfile("/home/hyun/mod_8psk.cplx64.pcm",dtype=np.complex64)
#plt.plot(samps[0:500])
#samps=np.fromfile("/home/hyun/works/QPSK/test.pcm",dtype='>i2') # big-endian
#plt.plot(samps[0:])
#plt.show()
#plt.plot(samps[320:])
#samps[320:].tofile("/home/hyun/works/QPSK/test_part3.pcm")
#plt.plot(samps[320:])
#plt.show()


