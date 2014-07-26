#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256
#define DICTIONARY_MAX_SIZE 50

typedef struct dictionary{
	char* words[DICTIONARY_MAX_SIZE] ; 
};

// Reads and prints dictionary
void readInput(char* filePath){
	FILE *file;
	char line[MAX_LINE];
	file = fopen(filePath, "r");
	while( fgets(line, MAX_LINE, file) ){
		printf("%s", line);
	}
	fclose(file);
}

int main(int argc, char *argv[]){
	char *dictionary = argv[1];
	char *text = argv[2];
	if( argc != 3 ){
		printf("standard use: %s dictionary input\n", argv[0]);
	}
	else{
		readInput(dictionary);
 	}	
}