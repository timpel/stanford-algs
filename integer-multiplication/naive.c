#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int toInt(char c){
	return c - '0';
}

int main(int argc, char *argv[]) {
	int i, j, product;
	char * n1 = argv[1];
	char * n2 = argv[2];
	int n1_len = strlen(argv[1]);
	int n2_len = strlen(argv[2]);

	for(j = n2_len - 1; j >= 0; j--){
		for(i = n1_len - 1; i >= 0; i--){
			product = toInt(n1[i]) * toInt(n2[j]);
			printf("%d\n", product);
		}
	}
	return 0;
}