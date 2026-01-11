def hanoi(start,dest,extra,n):
	if n ==1:
		print(f"Move from {start} to {dest}")
		return
	
	# Move n-1 disks to the extra peg
	hanoi(start,extra,dest,n-1)
	# Move the largest disk to the destination peg
	print(f"Move from {start} to {dest}")
	# Move the n-1 disks from the extra peg to the destination peg
	hanoi(extra,dest,start,n-1)

# Test the function with 3 disks
hanoi('A','B','C',3)
