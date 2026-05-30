

import numpy as np

import matplotlib.pyplot as plt

from SECLAB_signal import waveview_periodgram, plot_power, plot_time



def rotate_angle(samples,deg):    
    # type(samps) == complex!!!
    _rad=(2*np.pi)*(deg/360.0)  # py2에서 0이될 수 있음 그래서 360.0사용
    _rot=np.cos(_rad) + 1j*np.sin(_rad)     
    #print("_rad=",_rad)
    new_samples=samples*_rot
    return new_samples

plt.rcParams['figure.dpi']=80

path="/home/hyun/8psk_9.6k.cplx64.pcm"


samp_rate=8000
samps=np.fromfile(path,dtype=np.complex64) # '>i2' : big-endian

sync = samps[200:300]

#samps=samps[0:900] 
#samps=samps[0:]/32000. 
print("len(samps)=",len(samps))
plot_time(samps,'time: ')
plt.show()


f,pxx=waveview_periodgram(samps,samp_rate,1024,False)
plot_power(f,pxx,'power(periodgram): ')


corr=np.correlate(samps,sync,mode="full")
plot_time(corr[0:9000])


rot_sync=rotate_angle(sync,180) # 45 degree

corr=np.correlate(samps,rot_sync,mode="full")
plot_time(corr[0:9000])
