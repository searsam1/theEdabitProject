from datetime import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
	
	start = datetime.strptime(start_date, "%Y,%m,%d")
	end = datetime.strptime(end_date, "%Y,%m,%d")
	day_difference = (end - start).days
	if day_difference < 0:
		return "Invalid date"
	day_cost = stand * day_difference
	
	meter_reading = end_read - start_read
	if meter_reading < 0:
		return "Invalid meter readings"
	meter_cost = tariff * meter_reading
	
	total = round((meter_cost + day_cost) * 1.05,2)
	return "${0}".format(total)
	