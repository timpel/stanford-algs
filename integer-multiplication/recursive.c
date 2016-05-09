#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

int *strToIntArray(char *s, int len){
	int *intArray = malloc(sizeof(int) * len);
	int i;

	// convert each char to an int
	for(i = 0; i < len; i++){
		intArray[i] = s[i] - '0';
	}

	return intArray;
}

// populate a new array with half the values from the input array
int *splitIntArray(int *arr, int len, bool right){
	int *newArr = malloc(sizeof(int) * len/2);
	int i;

	// 'right' tag means get from second half of input
	if (right) {
		for(i = 0; i < len/2; i++) {
			newArr[i] = arr[i+len/2];
		} 
	}
	else {
		for(i = 0; i < len/2; i++) {
			newArr[i] = arr[i];
		} 
	}

	return newArr;
}

// convert int arrays back into integers
int arrToInt(int *arr, int len) {
	int i, j, tens;
	int result = 0;
	
	for(i = 0; i<len; i++){
		tens = 1;
		for(j = 0; j < i; j++){
			tens *= 10;
		}
		result += arr[len - 1 - i] * tens;
	}
	return result;
}

int multiply(int *n1, int len1, int *n2, int len2) {
	int n, term1, term2, term3;
	int *a, *b, *c, *d;

	// base case
	if (len1 == 1 || len2 == 1){
		return arrToInt(n1, len1) * arrToInt(n2, len2);
	}

	// split each input term in 2 and generate the 3 terms of the multiplication equation
	else {
		n = len1 > len2 ? len1 : len2;
		
		a = splitIntArray(n1, len1, 0);
		b = splitIntArray(n1, len1, 1);
		c = splitIntArray(n2, len2, 0);
		d = splitIntArray(n2, len2, 1);
		
		term1 = pow(10, n) * multiply(a, len1/2, c, len2/2);
		term2 = pow(10, n/2) * (multiply(a, len1/2, d, len2/2) + multiply(b, len1/2, c, len2/2));
		term3 = multiply(b, len1/2, d, len2/2);

		free(d);
		free(c);
		free(b);
		free(a);

		return term1 + term2 + term3;
	}
}

int main(int argc, char *argv[]) {
	int len1 = strlen(argv[1]);
	int len2 = strlen(argv[2]);
	
	int *n1 = strToIntArray(argv[1], len1);
	int *n2 = strToIntArray(argv[2], len2);
	
	int i, j;

	int product = multiply(n1, len1, n2, len2);

	printf("%d\n", product);

	free(n1);
	free(n2);
	
	return 0;
}
