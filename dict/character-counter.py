from collections import Counter 

s = "Hello World"
def character_counter():
    result = Counter(ch for ch in s.lower() if not ch.isspace())
    print(result)
    for key,value in result.items():
        print(f"{key} --> {value}")
if __name__ == '__main__':
    character_counter()
