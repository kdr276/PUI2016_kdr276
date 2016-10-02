# PUI 2016 HW4 - Kelsey Reid

## Assignment One - Peer Review

Performed peer review on ____ Citi Bike assignment. Her hypotheis 


## Assignment Two - Liturature Choices of Statistical Choices


| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
ANCOA	| 2, types of rats (SHR or WKY) | categorical | 1, route covered to locate food pellets in holeboard| continuous | N/A | N/A | 	Do SHRs show deficits in spatial working memory compared to WKYs | SHRs spatial working memory >= WKYs spatial working memory | 0.05 | [Spatial Memory in Spontaneously Hypertensive Rats (SHR)](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0074660)|
|||||||||


## Assignment Three - Reproduce the analysis of the Hard to Emplot Program in NY

I was unable to download the skeleton notebook into jupyter hub (attempted via wget within command line, received an error in jupyter re: not json file). Provided responses to blank/to do cells within .ipynb uploaded herein. Created a null hypothesis and preformed z test using formulas provided in the example and plugging in the appropriate variables based on the data I was working with. using the z-score table I determined that P was equal to .7995 and plugged the same into the formula created to determine if P < alpha. It was found that it was not and therefore the null hypothesis could not be rejected.
Following the example of the contingency table I created one for the question regarding recidivism. Using the formulas in the example I plugged in the values specific to recidivism. Using the chi-squared distribution table I determined that based on the degrees of freedom (1) and the minimum chi-squared significant value for alpha = 0.05 the null hypothesis could not be rejected. Results were found to fall between the critical values of .5 and .25 so no statistical significance could be identified. 

## Assignment Four -

Similar to assignment three I was unable to download the skeleton notebook into jupyter so I proceeded to create a new notebook reproducting the skeleton and including responses to blank/to do cells. I downloaded the csv table using the same method as done in HW3_kdr276 Assignment 2 (https://discuss.analyticsvidhya.com/t/how-to-read-zip-file-directly-in-python/1659/2) [https://discuss.analyticsvidhya.com/t/how-to-read-zip-file-directly-in-python/1659/2)

In order to pull 1 from every 200 rides I used the indexing method found on (http://www.webpages.uidaho.edu/~stevel/504/Pandas%20DataFrame%20Notes.pdf)[http://www.webpages.uidaho.edu/~stevel/504/Pandas%20DataFrame%20Notes.pdf]. Same resource used to select ageM rows that did not contain NaN fields, then used idex to pull 1084 rows to make the sample size the same as ageF. I created a separate dataframe for each of the two genders so I could manipulate the data without effecting the other column. I selected 1 out of every riders and then selected rows that did not contain NaN values. From the KS test it was determined that there were 1084 rows for the female data so I redacted the number of male samples to equal this number as the Pearson test required equal sized samples.

