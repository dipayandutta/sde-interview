#include <stdio.h>
#include <stdlib.h>

int main(int argc , char *argv[]){
	
	FILE *filenameSRC;
	FILE *filenameDEST;

	int ch;
	if (argc !=3){
		printf("Usage: %s: <filename>\n",argv[0]);
	}

	filenameSRC = fopen(argv[1],"r");
	filenameDEST = fopen(argv[2],"w");

	if (!filenameSRC || !filenameDEST){
		perror("fopen");
		return 1;
	}
	else{
		while((ch = fgetc(filenameSRC))!=EOF){
			fputc(ch,filenameDEST);
		}

	}
	fclose(filenameSRC);
	fclose(filenameDEST);

	return 0;
}
