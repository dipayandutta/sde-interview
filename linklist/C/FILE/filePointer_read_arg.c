#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	
	FILE *fp;
	char *filename;
	char buffer[100];

	filename = argv[1];
	fp = fopen(filename,"r");

	if (fp == NULL){
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
