import time

def dec_function(base_function):

	def calculate_time():
		start_time = time.time()
		base_function()
		end_time = time.time()
		print(f"Task Completed in : {end_time - start_time}")

	return calculate_time

@dec_function
def brew_tea():
	print("brewing the Tea....")
	time.sleep(1)
	print("Tea is Ready...")

@dec_function
def brew_coffee():
	print("Brewing the Coffee...")
	time.sleep(1)
	print("Coffee is ready...")

brew_tea()
brew_coffee()
