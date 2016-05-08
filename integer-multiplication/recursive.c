#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int* toInt(char * s, int len){
	int * arr = malloc(sizeof(char) * len);
	int i = 0;

	for(i = 0; i < len; i++) {
		arr[i] = s[i] - '0';
	}
	
	return arr;
}

int main(int argc, char *argv[]) {
	int n1_len = strlen(argv[1]);
	int n2_len = strlen(argv[2]);

	int * n1 = toInt(argv[1], n1_len);
	int * n2 = toInt(argv[2], n2_len);

	free(n2);
	free(n1);
	return 0;
}