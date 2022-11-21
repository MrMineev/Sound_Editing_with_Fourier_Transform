# importing libraries

import matplotlib.pyplot as plt
from sympy import ifft
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100 # frequency of are recording

data = [] # this is an array for storing the data from the recording
FT = [] # this is the array that stores the fourier transform of the recording

with open('data.txt', 'r') as f: # loading data from recording from file "data.txt"
    text = f.readlines() # reading all the lines
    mas = text[0].split('|') # spliting all the text for each element of mas to be one number matching to the pressure at that time
    for i in range(len(mas) - 1):
        st = mas[i][1:-1] # deleting simbol '[' and simbol ']'
        data.append(float(st)) # saving data
    f.close() # closing 'data.txt'

def plot_data(qwe): # this function will plot our array
    datax = [] # this is the index array for array 'qwe'
    for i in range(len(qwe)):
        datax.append(i) # appending the index of the element
    plt.plot(datax, qwe) # ploting the arrat 'qwe' with the indexing 'datax'
    plt.show() # showing the plot

def minus(l, r, value): # this function will change the value of all the elements of the fourier transform array from 'l' to 'r' to 'value'
    for i in range(l, r): # looping from l to r
        FT[i] = value # changing the value of the element to 'value'

FT = np.fft.fft(data) # calculating the fourier transform for the 'data' array

plot_data(data) # ploting the data to see the starting recording
plt.show() # showing the starting recording plot

# here we can change the value of the elements in the array FT (fourier transform)

# to change the values of different elements in the array FT you can use the function 'minus' for example if
#       you want to change all the elements from 100 to 150 to the value of 0 you write on the next line 'minus(100, 150, 0)'
#           so the first argument you get is the left index, the second argument is the right index, and the last argument is the value you want to give th elements

''' start changing the FT '''

''' end changing the FT '''

# the end where we can change the value of the elements in the array FT (fourier transform)

plot_data(FT) # ploting the fourier transform array
plt.show() # showing the fourier transform array plot

transform = np.fft.ifft(FT) # geting the new recording from the fourier transform using the inverse fourier transform

plot_data(transform) # ploting the new recording
plt.show() # showing the new recording plot

wv.write("result.wav", transform, freq, sampwidth=2) # saving the new recording in 'result.wav'

