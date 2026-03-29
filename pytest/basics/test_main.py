from main import get_weather 

def test_get_weather():
    assert get_weather(22) == "hot" 
    assert get_weather(10) == "cold"


'''
What is assert?
Python assert is a validation and debugging statement used to check if the condition is true
'''
