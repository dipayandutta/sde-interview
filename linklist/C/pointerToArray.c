/*
Pointer to an array means
A pointer that points to the entire array as one block, not to a single element.
*/

#include <stdio.h>

int main(){
	int arr[5] = {10, 20, 30, 40, 50};

	int (*ptr)[5] = &arr; //pointer to an array of 5 items

	for (int i = 0;i<5;i++){
		printf("%d",(*ptr)[i]);
	}

	return 0;
}


