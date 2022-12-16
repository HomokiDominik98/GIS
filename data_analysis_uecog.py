from scipy.io import loadmat
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

amplifier_Data = loadmat(r'C:\Users\User\Documents\PPKE ITK info-bionika\_HillierLab\FFT\amplifier1613.mat')
timeaxis_Data = loadmat(r'C:\Users\User\Documents\PPKE ITK info-bionika\_HillierLab\FFT\timeaxis161329_2.mat')

#extract the needed parts from the data
data_ = amplifier_Data['NeuralData']
t_ = np.transpose(timeaxis_Data['xTime'])


#selecting one of the channels of electrode
one_channel = data_[1]

is_control = False


#plotting the whole signal

def plottingOfSignal(t_, data_):
  #print(t_.shape)
  #print(data_[].shape)
  plt.plot(t_, data_)
  xlabel('Time[s]')
  ylabel('Channel voltage [uV]')
  plt.show()


#plotting all of the 32 channels at the same time in order to see which one wanst working -> turns out all of them were good
def plotting_32channels(t_,data_):
  for i in range(0,32,1):
      plt.subplot(32,1,1+i)
      plt.plot(t_, data_[i])
      #plt.subplot(2,1,2)
      #plt.plot(t_, data_[1])
      ylabel('Channel voltage [uV]')
      xlabel('Time[s]')
  plt.show()

def plotting_fft(one_channel, t_, title_, x_begin, x_end, x_label, y_label, name_save, is_control):
  x = one_channel.reshape(-1)
  #creating one dimensional array
  t = np.array(t_).squeeze()
  dt = t[1]-t[0]
  #total number of data points
  N = x.shape[0]
  #total duration of the data
  T = N * dt

  xf = fft(x-x.mean())
  Sxx = 2*dt**2 / T * (xf * xf.conj())
  Sxx = Sxx[:int((len(x) / 2))]

  df = 1/ T.max()
  fNQ = 1 / dt / 2
  if not is_control:
    faxis = arange(0,fNQ,df)
  elif is_control:
    faxis = arange(0,fNQ-df,df)

  plt.plot(faxis, Sxx.real)
  plt.title(title_)
  plt.xlim([x_begin,x_end])
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  #savefig(name_save)
  plt.show()





def fft_FromFirstMinute(one_channel, t_, title_, x_begin, x_end, x_label, y_label, name_save, is_control):
  x = one_channel[0:1200000].reshape(-1)
  #creating one dimensional array
  t = np.array(t_).squeeze()
  dt = t[1]-t[0]
  #total number of data points
  N = x.shape[0]
  #total duration of the data
  T = N * dt


  xf = fft(x-x.mean())
  Sxx = 2*dt**2 / T * (xf * xf.conj())
  Sxx = Sxx[:int((len(x) / 2))]

  df = 1/ T.max()
  fNQ = 1 / dt / 2
  if not is_control:
    faxis = arange(0,fNQ,df)
  elif is_control:
    faxis = arange(0,fNQ-df,df)

  plt.plot(faxis, Sxx.real)
  plt.title(title_)
  plt.xlim([x_begin,x_end])
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  #savefig(name_save)
  plt.show()

def fft_FromLastMinute(one_channel, t_, title_, x_begin, x_end, x_label, y_label, name_save, is_control):
  x = one_channel[0:1200000].reshape(-1) #creating one dimensional array
  t = np.array(t_).squeeze()
  dt = t[1]-t[0]
  #total number of data points
  N = x.shape[0]
  #total duration of the data
  T = N * dt
 

  xf = fft(x-x.mean())
  Sxx = 2*dt**2 / T * (xf * xf.conj())
  Sxx = Sxx[:int((len(x) / 2))]

  df = 1/ T.max()
  fNQ = 1 / dt / 2
  if not is_control:
    faxis = arange(0,fNQ,df)
  elif is_control:
    faxis = arange(0,fNQ-df,df)

  plt.plot(faxis, Sxx.real)
  plt.title(title_)
  plt.xlim([x_begin,x_end])
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  #savefig(name_save)
  plt.show()




plottingOfSignal(t_,data_)

#plotting_32channels(t_,data_)

#plotting_fft(one_channel, t_, "Spectrum", 0, 200, 'Frequency [Hz]', 'Power [$\mu V^2$/Hz]', 'img/155831', is_control)

#fft_FromFirstMinute(one_channel, t_, "Spectrum", 0, 200, 'Frequency [Hz]', 'Power [$\mu V^2$/Hz]', 'img/155831', is_control)

#fft_FromLastMinute(one_channel, t_, "Spectrum", 0, 200, 'Frequency [Hz]', 'Power [$\mu V^2$/Hz]', 'img/155831', is_control)