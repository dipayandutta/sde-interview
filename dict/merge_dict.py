d1 = {"a": 10, "b": 5}
d2 = {"b": 20, "c": 15}
d3 = {k: max(d1.get(k,0),d2.get(k,0)) for k in d1 | d2}
print(d3)
