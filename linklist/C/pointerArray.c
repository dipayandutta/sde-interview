#include <stdio.h>

int main(void){
	char *names[] = {
		"linux",
		"python",
		"c",
		"go"
	};

	int i;
	for(i=0;i<4;i++){
		printf("%s\n",names[i]);
	}

	return 0;
}
