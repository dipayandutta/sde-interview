myList = [1, 2, 3, 44, 4, -1, 10]
key = 10

def linear_search(myList,key):
    for item in range(len(myList)):
        if myList[item] == key:
            return True,item
    return False,-1

found,item = linear_search(myList,key)
if found:
    print(f"Item Found in {found} position {item}")
else:
    print("Not Found!")
