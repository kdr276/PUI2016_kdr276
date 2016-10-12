# PUI 2016 HW5 - Kelsey Reid

## Assignment One - Goodness of Fit Tests

I chose to use the Citi Bike data from 01/2015 and opened the csv file in the notebook with the same method as in the last two weeks (https://discuss.analyticsvidhya.com/t/how-to-read-zip-file-directly-in-python/1659/2)[(https://discuss.analyticsvidhya.com/t/how-to-read-zip-file-directly-in-python/1659/2]. Created a new column variable of age by subtracting the year the data was obtained (2015) from the birth year recorded for each subscriber ride - note: year of birth not recorded for 'user' rides.
Distribution of sample data reported a mean of 40. A histogram shows the data moving towards a normal distribution. 
Shared my notebook with group members Matt Slone, Will Xia, Marc Toneatto, and Ozgur Akkas for assistance in performing the second KS test with a different distribution than normal. Matt provided assistance in advising that the logistic distribution worked without having to provide any other arguments, which is also the distribution I chose for my second type of test, AD.



## Assignment Two - Line Fitting and Data Munging on Income Gender Bias

Created a new notebook to follow along with the skeleton notebook provided. Assigned each variable to a dataframe to serve as key-pair values with keys for dictionaries created for male and female data. I opened one of the excel files and found that the needed data started on line 10 so the header was set to start at position 9 so the appropriate data would be displayed. Assigned value pairs to keys and confirmed that the data is displaying correctly.

Plotted Total Median Income of females vs males by race. I created a point to represent the comparison by each race, pulling the appropriate row by calling index [1] for each median income category. Will Xia helped explain creating the 1-1 comparison line. Used the polyfit function as explained by Will Xia to perform a fit test. Created an array of median values by race for both male and female.

Shared with homework group my line of code to make the legends fit better within the space and not overlap plotted information i.e best location, remove bored, make font smaller. Made an income prediction based off of information seen in plot, used formula provided by Will Xia to test difference between male and female income based off of regression information that was produced.



## Assignment Three - Null Hypothesis Formulation

1.) The group of participants on a diet will lose more or the same amount of fat as the group of participants on an exercise regime 
H0: P(diet) > or = P(exercise)

2.) The percentage of Americans polled by Newsweek in 2016 will respond "yes" when asked if they trust the president will be more or equal to the percentage of Americans polled by Newsweek in 1994 that responded "yes" when asked if they trsut the president
H0: P(2016) > or = P(1994)
H0: P(20016) > or = 45%"

3.) Rate of smoking cessation for participants assigned to a nicotene patch is less than or equal to the rate of smoking cessation for participants assigned to a placebo patch
H0: P(nicotene) < or = P(placebo)

4.)The IQ of children ages 1-4 with mothers that smoked while pregnant is higher or equal to the IQ of children ages 1-4 with mothers that did not smoke while pregnant
H0: P(smoke) > or = P(nonsmoke)
