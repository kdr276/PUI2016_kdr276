# PUI 2016 HW11 - Kelsey Reid

## Assignment 1

Completed Assignment 1 on my own and shared notebook with homework group Will Xia, Matt Sloane, Marc Toneatto, and Ozgur Akkas. Group discussed process
Converting the coordinates was done by referencing the geospatial analysis lab notebook.
I knew I had to create a variable to store the index location of the CUSP containing polygon but kept running into an error 'too many values to unpack'. The only important lists(columns) for the query were the index location and geometry so I used the zip function to combine only those values(http://stackoverflow.com/questions/7999001/trouble-with-zip-function-in-for-loop-python). I stored the value of the index in a new variable to plot as the CUSP contained polygon

## Assignment 2

Downloaded census data for business by zipcode using the function provided in the instructional notebook. Only the years 1994-2014 were downloaded, an error was received for the years of 1993 and 2015 stating no file and no directory existing, respectively. 
Used a for loop to read the downloaded zipfiles as text files and combine all files into one data frame. Referenced (http://pandas.pydata.org/pandas-docs/stable/merging.html) to use concatenate for combining files then dropped all columns except for those for establishments, year, and zip code. The two datasets can be merged on the zipcode column but I was unable combine each est year column into a single row for each zip code.



