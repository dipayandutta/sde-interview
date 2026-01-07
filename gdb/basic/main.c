#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

	int numberOne = atoi(argv[1]);
	int numberTwo = atoi(argv[2]);

	if (numberOne == 5){
		printf("Value of First Number is %d",numberOne);
	}
	int result = numberOne+numberTwo;

	printf("Result=%d\n",result);

	return 0;
}
