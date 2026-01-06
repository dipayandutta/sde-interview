#include <stdio.h>

/*
	argc --> Argument Counter, Tells how many arguments were passed
	*argv--> An array of pointers of characters
*/
int main(int argc, char *argv[]){
	for(int i=0;i<argc;i++){
		printf("argv[%d]= %s\n",i,argv[i]);
	}
	return 0;
}
