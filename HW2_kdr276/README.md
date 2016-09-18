# PUI 2016 HW2 - Kelsey Reid

## Assignment One - Tracking Each Vehicle For a Line:

For this assignment I created a python script file that takes 2 arguments to report MTA API data of the number and location of buses of a given bus line. The first argument being the MTA key assigned to the specific user and the second being the desired bus line. 

Once I obtained my key I requested data from the BusTime API server and copied the data into a JSON formatter to better understand the hierarchy of nested dictionaries and lists. Once I could understand the specific keys to the information I wanted to report, I was able to make a print statement to print the information for the chosen bus line. I then created a loop with a counter to print a total of buses active on the chosen line and a loop to report the longitude and latitude of each active bus. Once I was confident the code ran properly I replaced my key and bus line information in the url with variables to represent the arguments to be passed from the command line.
Written and tested in Python 2.7 - imported print_function compatibility with Python 3

## Assignment Two - Next Stop information



## Assignment Three - Read CSV File With Pandas
Chose to use Emergency Response Incident .csv information from the datahub site. Confirmed os.getenf('DFDATA') pointed to correct data facility location
Difficulty opening the .csv file from this point with pandas, the DFDATA + datset location (/pasr-j7fb) did not point to .csv file which was located at another url (https://data.cityofnewyork.us/resource/pasr-j7fb.csv) -- to return and rework pulling of the file --
Used the .head() command to pull only the first 5 lines of the file and the .drop command to remove the all column headers except for two numerical - the longitude and lititue for each incident.
Plotted the cooridnate information using plot.scatter
