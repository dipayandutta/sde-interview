def merge_sorted_array(a,b):
	merged_array,i,j = [],0,0

	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			merged_array.append(a[i])
			i += 1
		elif a[i]>b[j]:
			merged_array.append(b[j])
			j +=1
		else:
			merged_array.extend([a[i],b[j]])
			i,j = i+1, j+1

	merged_array.extend(a[i:])
	merged_array.extend(b[i:])

	return merged_array
array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6, 8, 10]
print(merge_sorted_array(array1, array2))
