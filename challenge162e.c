#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256
#define DICTIONARY_MAX_SIZE 50

typedef struct Dictionaries {
	char* words[DICTIONARY_MAX_SIZE] ; 
} Dictionary;

void printDictionaryContents(Dictionary *dict, int numberOfItems){
	int i;
	for (i = 0; i < numberOfItems; i++)
		printf("%d: %s", i, dict->words[i]);
}

/*  Reads file contents and stores each word
 *	into a dictionary. 
 */
Dictionary* readInput(char* filePath){
	FILE *file;
	char line[MAX_LINE];
	Dictionary* dict = (Dictionary*) malloc(DICTIONARY_MAX_SIZE * sizeof(Dictionary));
	file = fopen(filePath, "r");
	int index = 0; 
	while( fgets(line, MAX_LINE, file) ){
		char *newChar = (char*) malloc( sizeof(char) * MAX_LINE);
		strcpy(newChar, line);
		dict->words[index] = newChar;
		index++;

	}
	fclose(file);
	return dict;
}

int main(int argc, char *argv[]){
	char *dictionary = argv[1];
	char *text = argv[2];
	if( argc != 3 ){
		printf("standard use: %s dictionary input\n", argv[0]);
	}
	else{
		Dictionary* dict = readInput(dictionary);
		printDictionaryContents(dict, 23);
 	}	
}