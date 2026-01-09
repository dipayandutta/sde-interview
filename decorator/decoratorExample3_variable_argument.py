import time

def dec_timer(base_function):
	def enhanced_function(*args):
		start_time = time.time()
		base_function(*args)
		end_time = time.time()
		print(f"Time taken to complete the task: {end_time-start_time}")
	return enhanced_function

@dec_timer
def brew_tea(tea_type,steep_time):
	print(f"Brewing {tea_type} tea...")
	time.sleep(steep_time)
	print(f"Tea is Ready...")

@dec_timer
def brew_coffee():
	print(f"Brewing coffee...")
	time.sleep(2)
	print(f"Coffee is Brewing...")

brew_tea("green",2)
brew_coffee()
