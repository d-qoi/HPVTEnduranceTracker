"""
Developed by Alexander Hirschfeld Apr 24, 2016
For the Rose-Hulman Human Powered Vehicle Team

See the read me for instructions

There is no warrenty for this
"""
import configparser
import time as Time


teamsFile = ""
distance = 0
backup = ""

teamList = {}
timeList = {}

def timeConvert(time):
	return str(time)

def readConfig():
	global distance,teamsFile, backup
	config = configparser.ConfigParser()
	config.read('config.conf')
	distance = float(config["DEFAULT"]["DISTANCE"])
	teamsFile = config['DEFAULT']['TEAMS']
	backup = config['DEFAULT']['BACKUP']
	print(distance, teamsFile, backup)


def readTeams():
	global teamList, teamsFile
	with open(teamsFile, 'r') as teams:
		for line in teams:
			data = line.strip().split(',')
			teamList[data[0].strip()] = data[1].strip()
			timeList[data[1].strip()] = []

def startRace(time):
	global backup
	with open(backup, 'a') as back:
		for teams in timeList.keys():
			timeList[teams].append(time)
			back.write(teams + " = " + timeConvert(time) + "\n")

def calcRank():
	global teamList, distance, timeList
	toSort = {}
	for team in teamList.keys():
		times = timeList[teamList[team]]
		dist = len(times) * distance
		if len(times) < 2:
			continue
		speed = dist/(times[-1] - times[0])
		toSort[team] = speed
	toSort = sorted(toSort, key=lambda split:split[1])
	toSort.reverse()
	return toSort

def main():
	global teamList, timeList, backup
	run = True
	start = False
	while run:
		userIn = input(":").lower()
		if "start" in userIn and not start:
			start = True
			startRace(Time.time())
			continue

		elif "list" in userIn:
			#print(teamList.keys())
			num = userIn.strip("list").strip()
			try:
				for t in timeList[num]:
					print(t)
				print(len(timeList[num]), 'laps')
			except:
				print("not a team")

		elif "rank" in userIn:
			for rank in calcRank():
				print(rank)

			continue

		elif "end" in userIn:
			run = False
			continue

		else:
			if not start:
				print("Race not Started")
				continue
			with open(backup,'a') as back:
				tm = Time.time()
				nums = userIn.split(' ')
				for num in nums:
					if num in timeList:
						timeList[num.strip()].append(tm)
						back.write(num + ' = ' + timeConvert(tm) + '\n')
					else:
						print(num,"is not a declared team")
			continue

if __name__ == "__main__":
	readConfig()
	readTeams()
	main()