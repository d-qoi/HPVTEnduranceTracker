# Rose-Hulman Institute of Technology Lap Counter Solution

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
	
	Start the race by typing _start_, hit enter when the flag is dropped

	After that, type the number of the team (as specified in the teams.csv) and hit enter
		More than one team can be specified at a time using spaces

	End the race with _end_ this will stop the timing and exit the program

### Other commands

* rank
	* This will list the teams in the order by average speed

* list ##
	* this will display all times recorded for #

* speed ##
	* this will give the average speed in km/hr
