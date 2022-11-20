# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import matplotlib.pyplot as plotter
import numpy as np
import math

freq = 44100 # the frequency of are recording

duration = 10 # the time duration of the recording

print("started") # print started to know when the computer started recodring

recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=1) # save the recording in the array recording

sd.wait()

write("recording0.wav", freq, recording) # this will convert the NumPy array to an audio with the given frequency 'freq'

# Convert the NumPy array to audio file
#wv.write("recording1.wav", recording, freq, sampwidth=2)

datax = [] # creating the index array for the recording
for i in range(len(recording)):
    datax.append(i) # appending the index

plotter.plot(datax, recording) # ploting the recording
plotter.show() # showing the recording plot

with open('data.txt', 'w') as f: # saving the recording in 'data.txt'
    for i in range(len(recording)):
        f.write(str(recording[i]) + "|") # writing the value in to 'data.txt'
    f.close() # closing the file