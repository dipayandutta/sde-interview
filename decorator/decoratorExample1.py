import time

# This is the decorator functiom
def timer_dev(base_function):
	# Defination of the enhanced function
	def time_calcualate():
		start_time = time.time()
		base_function()
		end_time = time.time()
		print(f"Task time: {end_time-start_time} seconds")
	
	return time_calcualate # Return the enhanced function


@timer_dev # <---- This is the decorator

# calling the base function
def brew_tea():
	print("Brewing the Tea ...")
	time.sleep(2)
	print("Tea is Ready!")

brew_tea()
