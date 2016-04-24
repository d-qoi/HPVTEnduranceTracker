"""
Developed by Alexander Hirschfeld Apr 24, 2016
For the Rose-Hulman Human Powered Vehicle Team

See the read me for instructions

There is no warrenty for this
"""
import configparser
import time

teamsFile = ""
startTime = 0;
distance = 0
backup = ""

teamList = {}
timeList = {}

def timeConvert(time):
	return time

def readConfig():
	config = configparser.ConfigParser()
	config.read('config.conf')
	disntace = float(config["DEFAULT"]["DISTANCE"])
	teamsFile = config['DEFAULT']['TEAMS']
	backup = config['DEFAULT']['BACKUP']


def readTeams():
	with open(teamsFile, 'r') as teams:
		for line in teams:
			data = line.strip().split(',')
			teamList[data[0].strip()] = data[1].strip()
			timeList[data[1].strip()] = []

def start(time):
	with open(backup, 'a') as backup:
		for teams in timeList.keys():
			timeList[teams].append(time)
			backup.write(teams + " " timeConvert(time))

def calcRank():
	toSort = {}
	for team in teamList.keys():
		times = timeList[team]
		dist = len(times) * disntace
		if len(times) == 0:
			continue
		speed = dist/(times[-1] - times[0])
		toSort[team] = speed
	return sorted(toSort, key=lambda split:split[1])

def main():
	run = True
	start = False
	while run:
		userIn = input(:)
		if userIn.contains("start") and not start:
			start = True
			start(time.time())
			continue

		elif userIn.contains("list"):
			num = userIn.strip("list").strip()
			for t in timeList[num]:
				print(t)
			continue

		elif userIn.contains("rank"):
			for rank in calcRank():
				print(rank)
			continue

		elif userIn.contains("end"):
			run = False
			continue

		else:
			tm = time.time()
			nums = userIn.split(' ').strip()
			for num in nums:
				timeList[num.strip].append(tm)
			continue

if __name__ == "__main__":
	readConfig()
	readTeams()
	main()