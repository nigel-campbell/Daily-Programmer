#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LINE 256
#define DICTIONARY_MAX_LENGTH 50
#define PARAGRAPH_MAX_LENGTH 30

typedef struct Dictionaries {
	char* words[DICTIONARY_MAX_LENGTH] ; 
} Dictionary;

typedef struct Paragraphs {
	char* lines[PARAGRAPH_MAX_LENGTH];
} Paragraph;

void printDictionaryFile(Dictionary *dict, int numberOfItems){
	int i;
	for (i = 0; i < numberOfItems; i++)
		printf("%d: %s", i, dict->words[i]);
}
void printCompressedFile(Paragraph *content, int numberOfItems){
	int i;
	for (i = 0; i < numberOfItems; i++)
		printf("%d: %s", i, content->lines[i]);
}

/*  Reads file contents and stores each word
 *	into a paragraph. 
 */
Paragraph* readCompressedFile(char* filePath){
	FILE *file;
	char line[MAX_LINE];
	Paragraph* content = (Paragraph*) malloc(PARAGRAPH_MAX_LENGTH * sizeof(Paragraph));
	file = fopen(filePath, "r");
	int index = 0;
	while( fgets(line, MAX_LINE, file) ){
		char *newLine = (char*) malloc( sizeof(char) * MAX_LINE);
		strcpy(newLine, line);
		content->lines[index] = newLine;
		index++;
	}
	fclose(file);
	return content;
}

Dictionary* readDictionary(char* filePath){
	FILE *file;
	char line[MAX_LINE];
	Dictionary* dict = (Dictionary*) malloc(DICTIONARY_MAX_LENGTH * sizeof(Dictionary));
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
	char *compressedFile = argv[2];
	if( argc != 3 ){
		printf("standard use: %s dictionary input\n", argv[0]);
	}
	else{
		Dictionary* dict = readDictionary(dictionary);
		Paragraph* text = readCompressedFile(compressedFile);
		printCompressedFile(text, 6);
		printDictionaryFile(dict, 23);
 	}	

}