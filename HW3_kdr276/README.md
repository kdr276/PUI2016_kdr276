# PUI 2016 HW3 - Kelsey Reid

## Assignment One - Demonstrating Central Limit Theorem:

Using the example done in class to plot a chi squared distribution I changed the functions according to the desired type of distribution. I chose to use 100 as the mean for all distributions and chose the uniform distribution as my 5th distribution. Utilizing the scipy.org resource and Wikipedia to compare function parameters along with the distribution means, I applied the appropriate parameters within each function to ensure each mean was 100. All of the scatter plots and histograms displayed show that the distribution of means are normally distributed. If the same analysis were run with even more samples this normal distribution would be more apparent. 



## Assignment Two - CitiBike Data Data-Driven Inference:

Bailey Griswald shared the below link to help in downloading the date directly into the notebook from the Citi Bike data
[https://discuss.analyticsvidhya.com/t/how-to-read-zip-file-directly-in-python/1659/2](https://discuss.analyticsvidhya.com/t/how-to-read-zip-file-directly-in-python/1659/2)

Worked with Marc Toneatto, Matt Slone, Ozgur Akkas to develop hypothesis and complete assignment. Ozgur developed the first hypothesis which we as a group refined to address usage amoung types user types. 

After using the .drop function to remove the unwanted information, we had to assign numerical values to represent the options for 'usertype' so that they coud be plotted. We assigned 1 for a subscriber and 2 for a customer. I replaced these strings with the determined values using the .replace method following the example I found on Stackoverflow at [http://stackoverflow.com/questions/17142304/replace-string-value-in-entire-dataframe] (http://stackoverflow.com/questions/17142304/replace-string-value-in-entire-dataframe) which was shared while doing group work. I then reviewed the cvs file to determine a line where the response should be 2 for customer and used the .head function to show that line which allowed me to confirm the .replace function worked. We were then able to utilize the code in the example notebook by subing in our data to plot the usage by user type according to the dat of the week. Matt provide the function to change the limit on the y axis to make the plot easier to read.


## Assignment Three - Z-Test Lab

I formulated a null and alternative hypothesis regarding the change in bus commute times. The alternative hypothesis being what I expected to be true and the null hypothesis being the opposite I would try to reject based on further statistical tests.
Information on the mean and standard deviation of the old commute time data was provided in the lecture slides along with the sample size (which was also confirmed by openeing and reviewing the times.txt information)
I used the .mean() function to determine the mean of the sample which was rounded up to 34.5 and entered that into the z test formual to obtain a result of 2.5
This result was further than 2 signmas away from the old mean which allowed us to reject the null hypothesis. 
