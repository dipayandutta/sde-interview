#include <stdio.h>

int max(int a, int b){
	return (a>b) ? a:b;
}

int maxSum(int arr[],int n, int k){

	if (n <k) 
		return -1;
	int current_sum = 0;

	// Compute the first window
	for (int i=0;i<k;i++){
		current_sum += arr[i];
	}

	int max_sum = current_sum;

	// Slide the window from the left to right
	for (int i=k;i<n;i++){
	// Add the next element, subtract the first element of the the previous window
	current_sum += arr[i]-arr[i-k];
	max_sum = max(max_sum,current_sum);
	}

	return max_sum;

}

int main(void){
	int arr[] = {1, 4, 2, 10, 2, 3, 1, 0, 20};
	int k = 4;
	int n = sizeof(arr)/sizeof(arr[0]);// To Calculate the Length of the array
	int result;
	result = maxSum(arr,n,k);
	printf("%d",result);

	return 0;
}
