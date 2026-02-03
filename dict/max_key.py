data = {"cpu": 40, "mem": 70, "disk": 55}
max_key=max(data,key=data.get)
print(max_key)
