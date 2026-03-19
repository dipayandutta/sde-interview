s = "abaaaba"

half = len(s)//2
print(half)

pal = s[::-1]
if s == pal:
    print("Palindrom!")
