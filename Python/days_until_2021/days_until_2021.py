from datetime import datetime
def days_until_2021(date):
	now = datetime.strptime("2021","%Y") - datetime.strptime(date, "%m/%d/%Y")
	days = int(str(now).split("days")[0])
	return "{} day{}".format(days, ["","s"][days > 1])
	
res = days_until_2021("05/31/2020")
print(res)