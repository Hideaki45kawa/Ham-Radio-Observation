#!/usr/bin/python3.6

import numpy as np
import matplotlib
matplotlib.use('SVG')
import matplotlib.pyplot as plt
cdir='/mnt/drv1/test'

f=open(cdir+'/filename.dat')
fnn=f.readlines()
f.close()
#cdir=os.getcwd()
fo=fnn[0].split('.')
u=np.loadtxt(cdir+fo[1]+'.dat')

#print(u.shape)

xlab=np.arange(0,u.shape[0]+60,60)


plt.figure('Spectrogram')

ymax=3000
ylab=np.arange(0,u.shape[1],ymax/10)
asp=np.max(xlab)/ymax

plt.imshow(u.T,aspect=asp)
plt.xticks(xlab)
plt.yticks(ylab)
plt.ylim([0,ymax])
plt.ylabel('Freq.(Hz)')
plt.xlabel('Time(sec)')

fo2=fo[1].split('/')
plt.title(fo2[1])
#print(cdir+'/'+fo2[1]+'.png')
plt.savefig(cdir+'/'+fo2[1]+'.png')

plt.close()

