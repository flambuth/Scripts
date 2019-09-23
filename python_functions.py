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

def make_time_stamp(amount):
	time_stamp = f"{datetime_to_string()} {amount}"
	return time_stamp

def sayhello():
    print("Hello,world!")

if __name__ == '__main__':
    print('Hello, World!')

##############

def normalize_name(phrase): 
    if phrase[0].isalpha() == False:
        phrase = phrase[1:]
    phrase = phrase.strip() 
    phrase = phrase.replace(" ","_") 
    phrase = phrase.lower() 
    return phrase 

###########

def cumsum(*args):
    """ Returns a list that is the cumulative sum of the sequence of intengers passed as arguments """ 
    count = 0 
    cum_list = [] 
    for i in args: 
    #This is the starting condition. The rules change after the first argument is cemented at index 0
        if count == 0: 
            cum_list.append(i) 
            count = i 
    #Add to the list that will be returned the sum of next argument and the last one, stored in count 
    #and becomes the new count for the next round of the iteration
        else:
            cum_list.append(i+count) 
            count = i+count 
    return cum_list    

##############

def right_now_in_24hr():
    import datetime
#make a datetime object and cut out the hour and minutes using the string
#formatting method the object has. Using a %to indicate what to slice
#that method will not take more than 1 argument
    x = datetime.datetime.now()
    hour = x.strftime("%H")
    mins = x.strftime("%M")
#using fstrings to format these non-strings into some string output
    return f"It is {hour}{mins} hours"


##############

def capitalize_dicts_in_a_list(list_of_dicts): 
	"""
	Returns a dictionary that is the same one entered in parameters, but with the values
	capitalized.
	"""
	cap_dict_list = [] 
	for i in list_of_dicts: 
		cap_dict = {k:v.capitalize() for (k,v) in i.items()} 
		cap_dict_list.append(cap_dict) 
	return cap_dict 
