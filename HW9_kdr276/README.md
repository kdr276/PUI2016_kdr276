# PUI 2016 HW 9 - Kelsey Reid

## Assignment One - Time Series Analysis:

Worked with homework group Marc Toneatto, Matt Sloane, Ozgur Akkas, and Will Xia

Downloaded a copy of the .npy file into my directory to be able to open it and proceeded to replace the -1 values with NaN. Due to this future use of functions for mean and standard deviation will be numpy.nan___ (sum, mean, etc) to account for these values

For task one I created variables to sum various sides of the 3D array based on all stations, all ride types, and then stations and ride types for all 194 weeks. I also created a variable with the pandas.date_range to start at 5/21/2010 and run through a 194 week period. Plotted the total of stations and ride types for each week by the week interval variable and used the np.log10 function to make the plot more easily readable. Referencing the FDNYdeaths.ipynb file the threshold was calculated for plus or minus 3 points of the standard deviation  of the total for all weeks. A new plot was created with lines to represent the thresholds above and below the standard deviation. Using the numpy.where function we identified the week interval that fell below the lower threshold to be the week of 10/21/2012. Based on personal knowledge the group anticipated  the event to be caused by Hurricane Sandy; the below news article confirmed that the hurricane occured during this time period. At some point the subway was shut down and then many lines were not in service due to damage.
(http://www.cnn.com/2013/07/13/world/americas/hurricane-sandy-fast-facts/)


For task two we had to transpose the array for the sum of all ride types so that the length of the array matched that of the week interval variable. Matt determined the code needed to calculate the rolling mean of the sum of all ride types which was plotted against the week interval. Set up the ratio for first ten and last 10 weeks but could not determine how to proceed


For task three the array for the sum of rides at each station had to be transposed to plot against the week interval variable. I then used this same variable to represent N in the Fourier Transformation for the number of data points (194 weeks). As demonstrated in the fourier example notebook I started the plot at [1:] to omit the first value. A for loop was used to plot each of the 600 stations. Based on the example notebook I understood that (1/np.fft.rfftfreq(N, 1.0)[-1]) was equal to a two week period so through trial and error of changing the index location I found that [4] was the closest to 52 weeks at 48.5 weeks


