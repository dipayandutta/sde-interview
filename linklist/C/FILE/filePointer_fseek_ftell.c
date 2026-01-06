#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	
	char buffer[100];
	char *filename;

	filename = fopen(argv[1],"r");

	if (filename == NULL){
		perror("fopen");
		return 1;
	}
	else{
		fseek(filename,0,SEEK_END);
		long size = ftell(filename);

		printf("File Size: %ld bytes\n",size);
	}
	fclose(filename);
	return 0;
}
