myList=[1,2,3,44,4,-1,10]
key = 10

def searchBinary(myList,key):
    # sort the list
    arr = sorted(myList)
    print("Sorted List: ",arr)
    first = 0
    last = len(arr)-1
    print("Last is ",last)
    foundFlag = False
    while(first<=last):
        mid = (first+last)//2
        print("Checking index: ",mid, "Value:", arr[mid])
        if arr[mid] == key:
            return True,mid
        else:
            if key < arr[mid]:
                last = mid -1
                print("Now ",last)
            else:
                first = mid+1
                print("Now ",first)
    return False,-1

found,index = searchBinary(myList,key)

if found:
    print(f" key {key} found at the index {index}")
else:
    print(f"Key Not Found!")
