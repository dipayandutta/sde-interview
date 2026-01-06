#include <stdio.h>
#include <stdlib.h>

int main(void){
	FILE *fp;
	fp = fopen("output.txt","w");

	if (!fp){
		perror("fopen");
		return 1;
	}

	else{
		fprintf(fp,"LINUX SYSTEM PROGRAMMING\n");
		fprintf(fp,"FILE POINTER EXAMPLE\n");

		fclose(fp);
	}

	return 0;
}
