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
startTime = 0
homeNumber = 0;

teamList = {}
timeList = {}

def timeConvert(time):
	return str(int(time))

def prettyTime(time):
	hours = int(time/3600)
	time -= hours*3600
	minute = int(time/60)
	time -= minute*60
	return "%d:%d:%d"%(hours,minute,time)

def readConfig():
	global distance,teamsFile, backup, homeNumber
	config = configparser.ConfigParser()
	config.read('config.conf')
	distance = float(config["DEFAULT"]["DISTANCE"])
	teamsFile = config['DEFAULT']['TEAMS']
	backup = config['DEFAULT']['BACKUP']
	homeNumber = config['HOME']['NUMBER']
	print(distance, teamsFile, backup, homeNumber)


def readTeams():
	global teamList, teamsFile
	with open(teamsFile, 'r') as teams:
		for line in teams:
			data = line.strip().split(',')
			teamList[data[0].strip()] = data[1].strip()
			timeList[data[1].strip()] = []

def startRace(time):
	global backup,startTime,timeList
	startTime = time
	time -= startTime
	with open(backup, 'a') as back:
		for teams in timeList.keys():
			timeList[teams].append(time)
			back.write(teams + " = " + timeConvert(time) + "\n")

def stopRace(time):
	global backup, startTime, timeList
	time -= startTime
	with open(backup, 'a') as back:
		for team in timeList.keys():
			timeList[team].append(time)
			back.write(team + " = " + timeConvert(time) + "\n")

def calcRank():
	global teamList, distance, timeList
	toSort = {}
	for team in teamList.keys():
		times = timeList[teamList[team]]
		dist = len(times) * distance
		if len(times) < 2:
			continue
		speed = dist/(times[-1])
		toSort[team] = speed
	toSort = sorted(toSort, key=lambda time:toSort[time])
	toSort.reverse()
	return toSort

def main():
	global teamList, timeList, backup,startTime, distance, homeNumber
	run = True
	start = False
	while run:
		userIn = input(": ").lower()
		#print(userIn)
		if "start" in userIn and not start:
			start = True
			startRace(Time.time())
			continue

		elif "list" in userIn:
			#print(timeList.keys())
			num = userIn.strip("list ")
			print(num)
			try:
				for t in timeList[num.strip()]:
					print(prettyTime(t))
				print(len(timeList[num]), 'laps')
			except:
				print("not a team, listing teams by name")
				for key in teamList.keys():
					print(key + " : " + teamList[key])

		elif "rank" in userIn:
			for rank in calcRank():
				print(rank)

			continue

		elif 'speed' in userIn:
			num = userIn.strip("speed ").strip()
			try:
				print(len(timeList[num])*distance*3600/timeList[num][-1])
			except:
				print("something happened")
				start = False
				stopRace(Time.time())
				continue

		elif "stop" in userIn:
			start = False
			stopRace(Time.time())
			continue

		elif "end" in userIn:
			run = False
			continue

		else:
			if not start:
				print("Race not Started")
				continue
			with open(backup,'a') as back:
				tm = Time.time() - startTime
				nums = userIn.split(' ')
				for num in nums:
					if num in homeNumber:
						print(prettyTime(tm - timeList[num][-1]))
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