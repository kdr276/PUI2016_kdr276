# PUI 2016 HW 9 - Kelsey Reid

## Assignment One - Time Series Analysis:

Worked with homework group Marc Toneatto, Matt Sloane, Ozgur Akkas

Downloaded a copy of the .npy file into my directory to be able to open it and proceeded to replace the -1 values with NaN. Due to this future use of functions for meana nd standard deviation will be numpy.nan___ (sum, mean, etc) to account for these values

For task one I created variables to sum various sides of the 3D array based on all stations, all ride types, and then stations and ride types for all 194 weeks. I also created a variable with the pandas.date_range to start at 5/21/2010 and run through a 194 week period. Plotted the total of stations and ride types for each week by the week interval variable and used the np.log10 function to make the plot more easily readable. Referencing the FDNYdeaths.ipynb file the threshold was calculated for plus or minus 3 points of the standard deviation  of the total for all weeks. A new plot was created with lines to represent the thresholds above and below the standard deviation. Using the numpy.where function we identified the week interval that fell below the lower threshold to be the week od 10/21/2012. Based on personal knowledge the group antcipated the event to be caused by Hurricane Sandy; the below news article confirmed that the subway was shutdown during the same week interval due, as anticipated, to the hurricane.

For task two we had to transpose the array for the sum of all ride types so that the length of the array matched that of the week interval variable. Matt determined the code needed to calculate the rolling mean of the sum of all ride types which was plotted against the week interval.


'


(http://www.huffingtonpost.com/2012/10/28/mta-shutdown-hurricane-sandy-subway-cuomo_n_2034337.html)
