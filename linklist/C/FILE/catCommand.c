#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	FILE *fileName;
	char buffer[100];

	char ch;

	if (argc != 2){
		        printf("Usage: %s <file>\n", argv[0]);
		return 1;
	}
	
	fileName = fopen(argv[1],"r");
		if (!fileName){
			perror("fopen");
			return 1;
		}
		else{
			while ((ch =  fgetc(fileName)) !=EOF){
				putchar(ch);
			}
		}
	fclose(fileName);
	return 0;
}


