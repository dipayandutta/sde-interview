import time
from datetime import datetime,timedelta

def dec_timer(base_function):

	def enhanced_function(*args,**kwargs):
		start_time = time.time()
		result=base_function(*args,**kwargs)
		end_time = time.time()
		print(f"Time Taken to complete the task: {end_time-start_time} seconds")
		return result
	return enhanced_function


@dec_timer
def brew_tea(tea_type,steep_time):
	print(f"Brewing {tea_type} started ...")
	time.sleep(steep_time)
	print(f"Tea is Ready")

@dec_timer
def brew_coffee():
	print(f"Brewing Coffee is started ...")
	time.sleep(1)
	print(f"Coffee is Ready")
	return f"Drink Coffee by {datetime.now()+timedelta(minutes=30)}"

brew_tea(tea_type="Green",steep_time=1)
print(brew_coffee())
