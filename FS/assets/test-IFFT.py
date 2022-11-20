import matplotlib.pyplot as plt
from sympy import ifft
from sympy import fft
import numpy as np
  
# sequence 

def getSinData():
    ans = []
    inc = 0.1
    for i in range(int(10 / inc)):
        qwe = i * inc
        ans.append(np.sin(qwe))
    return ans


da = getSinData()

seq = np.fft.fft(da) / len(da)
seq = seq[range(int(len(da)/2))]

def getIndex(mas):
    ans = []
    for i in range(len(mas)):
        ans.append(i)
    return ans

plt.plot(getIndex(da), da)
plt.show()

plt.plot(getIndex(seq), seq)
plt.show()
  
# fft
transform = np.fft.ifft(seq)
print ("Inverse FFT : ", transform)

plt.plot(getIndex(transform), transform)
plt.show()