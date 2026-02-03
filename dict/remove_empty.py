data = {"host": "localhost", "port": None, "ssl": True}

cleaned = {k:v for k,v in data.items() if v is not None}
print(cleaned)
