import time 

def brew_tea():
	# start time of the function
	start_time = time.time()
	start_time = time.time()
	print("Brewing Tea...")
	time.sleep(1)
	print("Tea is ready")
	# end time of the function
	end_time = time.time()
	print(f"Task time: {end_time-start_time} seconds")


brew_tea()
