from collections import Counter

s = "Hello World"
char_count= Counter(s)
space=0
for ch,cnt in sorted(char_count.items()):
    if ch == " ":
        space += 1
    elif ch != " ":
        print(f"{ch}: {cnt}")
print(f"Total number of Spaces : {space}")
