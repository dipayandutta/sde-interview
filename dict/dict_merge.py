d1={'a':10}
d2={'b':20}

print(d1)
print(d2)

for k,v in d1.items():
    print(k,v)

for k,v in d2.items():
    print(k,v)

#merge dict
d3 = {**d1,**d2}
print(d3)

for k,v in d3.items():
    print(k,v)
