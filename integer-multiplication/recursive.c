#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int* toInt(char * s, int len){
	int * arr = malloc(sizeof(int) * len);
	int i = 0;

	for(i = 0; i < len; i++) {
		arr[i] = s[i] - '0';
	}
	
	return arr;
}

int** getabcd(int *arr1, int *arr2, int len1, int len2){
	int i,j;
	int *a = malloc(sizeof(int*) * (len1 / 2));
	int *b = malloc(sizeof(int*) * (len1 / 2 + (len1 % 2)));
	int *c = malloc(sizeof(int*) * (len2 / 2));
	int *d = malloc(sizeof(int*) * (len2 / 2 + (len2 % 2)));
	int **abcd = malloc(sizeof(int*) * 4);

	for(i = 0; i < len1/2; i++){
		a[i] = arr1[i];
		b[i] = arr1[i+len1/2];
	}
	if (len1 % 2) {
		b[i] = arr1[len1 - 1];
	}

	for(i = 0; i < len2/2; i++){
		c[i] = arr2[i];
		d[i] = arr2[i+len2/2];
	}
	if (len2 % 2) {
		d[i] = arr2[len2 - 1];
	}

	abcd = (int*[4]){a,b,c,d};

	return abcd;
}

int main(int argc, char *argv[]) {
	int n1_len = strlen(argv[1]);
	int n2_len = strlen(argv[2]);

	int * n1 = toInt(argv[1], n1_len);
	int * n2 = toInt(argv[2], n2_len);
	int i,j;
	int **abcd = getabcd(n1, n2, n1_len, n2_len);

	free(n2);
	free(n1);
	return 0;
}