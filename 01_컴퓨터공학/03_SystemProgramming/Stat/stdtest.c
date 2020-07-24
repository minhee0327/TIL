#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char** argv){
	char buf[255];
	FILE* fp;
	if(argc ==2){
		fp = fopen(argv[1],"r");
		if (fp==NULL){
			fputs("file open error", stderr);
			exit(0);
		}
	}else{
		fp=stdin;
	}while(fgets(buf, 255, fp) != NULL){
		fputs(buf, stdout);
	}
}
