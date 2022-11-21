# Sound Editing with Fourier Transform

This is a fourier transform based sound editing code.

How to use it?

1. Open file assets/recoring.py and run it. After on your terminal you see a message "started", you may start recording what ever you want

2. To check your recording you can open file 'recording0.wav'

3. Now open file assets/change_array run this file and the first thing you will see is a chart of your recording. After closing this chart another chart
will pop out. This chart is the fourier transform of your recording. You can change this fourier transform array on line 46 where i have explained how
to change the value of the elements in the fourier transform array. After closing this plot you will get a plot of a new recording bassed on the changes
in the fourier transform array

4. Know you can open the file 'result.wav' and see the new recording

How is it useful?

For example you have a recording with some awful sounds in the background like this one : [recording0.wav.zip](https://github.com/Dragon267/Sound_Editing_with_Fourier_Transform/files/10059047/recording0.wav.zip)

When you run the file 'change_array.py' you will get first the plot with the recording and after you close it you get the fourier transform plot that for this recording looks like this.

<img width="582" alt="Screenshot 2022-11-21 at 18 26 09" src="https://user-images.githubusercontent.com/112898086/203120916-f9dadfa6-c878-4faf-8566-1e103e30e722.png">

The spikes in the plot are the awful sounds in the background (we see the bad sounds in the background because they were pure sin waves, if the sounds you
want to remove aren't sin waves you will have to play around a bit with different changes of the fourier transform). If you take the left and the right indexes of all the spikes and remove them you will delete the bad sound in the background.

In this example you can write these lines of code in the file 'change_array.py' on line 46:

minus(15000, 55000, 0)

minus(385000, 425000, 0)

After you add these lines add run the code again you will get in the file 'result.wav' this : [result.wav.zip](https://github.com/Dragon267/Sound_Editing_with_Fourier_Transform/files/10059134/result.wav.zip)


You can play around with different recordings and different background sounds and try deleting them using fourier transform.
