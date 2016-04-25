# Rose-Hulman Institute of Technology Lap Counter Solution

	This is a lap counter and statistics tool for the HPRA and ASME human powered vehicle competition, specifically the endurance event.
	Everything in this is licensed under MIT, please read the included license file for details

	This was written for python 3.x.x 

## Use


	This is a replacement for the cheat sheet that we had at one point in time

### How to setup


	There is a _teams.csv_, Rose Hulman is use as an example
	The layout will be 

> Name, ##

	This will be read into the program once it is started

	There is a config file _config.conf_

	This will contain some of the specifics of the race

> Distance = 1.5

	This is the distance in Kilometers


### During the race
	
	Start the race by typing *start*, hit enter when the flag is dropped

	After that, type the number of the team (as specified in the teams.csv) and hit enter
		More than one team can be specified at a time using spaces

	Stop the race with *stop* this will stop the timing, and give everyone a last lap time

	End will exit the program



### Other commands

* rank
	* This will list the teams in the order by average speed

* list ##
	* this will display all times recorded for #

* speed ##
	* this will give the average speed in km/hr
