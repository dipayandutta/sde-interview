import time

def dec_timer(base_function):
	def enhanced_function(*args,**kwargs):
		start_time = time.time()
		base_function(*args,**kwargs)
		end_time = time.time()
		print(f"Time Taken to Complete the Task: {end_time-start_time}")

	return enhanced_function

@dec_timer
def brew_tea(tea_type,steep_time):
	print(f"Brewing tea {tea_type}...")
	time.sleep(steep_time)
	print(f"Tea is ready...")

@dec_timer
def brew_coffee(coffee_type,coffee_beans,steep_time):
	print(f"Brewing {coffee_type} from {coffee_beans}...")
	time.sleep(steep_time)
	print("Coffee is Ready...")

brew_tea(tea_type="green",steep_time=2)
brew_coffee(coffee_type="Espresso",coffee_beans="Africa",steep_time=1)
