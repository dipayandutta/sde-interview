# Regular Array
my_list = ["apple","banana","cherry"]
print(my_list)
print(my_list[1])


# Associative Array (Dictonary) Example
my_dict = {
		"fruitName": "apple",
		42:"banana",
		(1,2):"cherry"
}

#print(my_dict[1]) # This will show an error as the key is not present
print(my_dict["fruitName"])
print(my_dict[42])


# update the value associated with a key
my_dict["fruitName"] = "Orange"
print(my_dict["fruitName"])
