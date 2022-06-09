from datetime import datetime
def days_until_2021(date):
	now = datetime.strptime("2022","%Y") - datetime.strptime(date, "%m/%d/%Y")
	days = int(str(now).split("days")[0]) - 365
	return "{} day{}".format(days, ["","s"][days > 1])
	
