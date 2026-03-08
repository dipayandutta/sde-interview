'''
Question - Implement a split(s,c) method , which receivs a string and a character c and splits s at each occurance of c, returning an array of string.

Edge Cases
-----------
[1]. If s is emptry, should we return an empty list?
[2]. If s starts with c , should we return an empty string at the begining of the list
[3]. If s ends with c , should we return an empty string at the end of the list
[4]. If There are two consicutive occurence of c , should we add an empty string?

Example 
s = "/home/./..//Documents/",c='/'
output = ["","home","",".","",".",".","Documents",""]
'''
s = "/home/./..//Documents/"
c='/'
def split_function(s,c):
    result = []
    current = ""

    for ch in s:
        if ch == c:
            result.append(current)
            current = ""
        else:
            current+=ch
    result.append(current)
    return result

output=split_function(s,c)
print(f"{output}")

string="/home"
ch = "/"
def split_method(string,ch):
    result = []
    current = ""

    for chr in string:
        if chr == ch:
            result.append(current)
            print(f"Current Result --> {result}")
            current = ""
            print(f"Value of current -> {current}")
        else:
            current += chr
            print(f"Inside else the value of current is --> {current}")
    result.append(current)
    return result

output_1 = split_method(string,ch)
print(output_1)

