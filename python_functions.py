##Lets build our own module. Lambpy
def datetime_to_string(): 
	
	"""
	This takes the datetime object created when you call the now function. Cuts up the date attributes into
	a string variable with /'s in between.
	#
	# This doctest will need its own daily switch to test properly.
	# >>> datetime_to_string():
	'2019/9/18'

	"""
	import datetime 
	x = datetime.datetime.now() 
	string_date = f"{x.year}/{x.month}/{x.day}-{x.hour}:{x.minute}" 
	return string_date

def make_time_stamp(amount)
	time_stamp = f"{datetime_to_string()} {amount}"
	return time_stamp