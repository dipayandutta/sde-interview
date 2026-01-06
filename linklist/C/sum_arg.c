#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	int i;
	int numberOne;
	int numberTwo;
  numberOne = atoi(argv[1]);
	numberTwo = atoi(argv[2]);

	int sum = numberOne + numberTwo;
	printf("sum = %d\n",sum);

	return 0;
}
