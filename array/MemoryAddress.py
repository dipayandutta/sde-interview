import numpy as np

# Define contiguous array
arr = np.array([10, 20, 30, 40, 50, 60], dtype=np.int32)

element_index = 2

# Base memory address
base_address = arr.__array_interface__['data'][0]

# Element address calculation
element_address = base_address + element_index * arr.itemsize

print("Base address   :", hex(base_address))
print("Element address:", hex(element_address))
print("Value          :", arr[element_index])

'''

Internal Representation

list object
 └── array of pointers ──► PyObject* ──► int object (10)
                         ──► PyObject* ──► int object (20)
                         ──► PyObject* ──► int object (30)
'''
