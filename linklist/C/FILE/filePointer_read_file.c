/*
fopen() returns a file pointer which represents an open file stream, and fgets() reads data safely line by line.
*/
#include <stdio.h>
#include <stdlib.h>

int main(void){
	FILE *fp;
	char buffer[100];

	fp = fopen("test.txt","r");
	if (fp==NULL){
		perror("fopen");
		return 1;
	}
	else{
		while(fgets(buffer,sizeof(buffer),fp)){
			printf("%s",buffer);
		}
	}
	fclose(fp);
	return 0;
}
