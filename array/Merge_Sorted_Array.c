#include <stdio.h>
#include <stdlib.h>

int* merge_sorted_arrays(int* a, int n, int* b,int m, int* out_size){

	int i=0,j=0,k=0;

	// Allocate the result array
	int* merged = malloc((n+m) *sizeof(int));
	
	if (!merged) return NULL;

	// Merge while both arrays have the elements
	while (i<n && j<m){
		if (a[i]<b[j]){
			merged[k++] = a[i++];
		}
		else if (a[i] > b[j]){
			merged[k++]= b[j++];
		}else{
			// Equivalent of python merged_array.extend()
			merged[k++] = a[i++];
			merged[k++] = b[j++];
		}
	}
// Equivalent of merged_array.extend(a[i:])
while (i<n){
	merged[k++] = a[i++];
}

// Equivalent of merged_array.extend(b[j:])
while (j<m){
	merged[k++]= b[j++];
}

*out_size = k;
return merged;

}

int main() {
    int a[] = {1, 3, 5};
    int b[] = {2, 3, 4};

    int out_size;
    int* result = merge_sorted_arrays(a, 3, b, 3, &out_size);

    for (int i = 0; i < out_size; i++) {
        printf("%d ", result[i]);
    }

    free(result);
    return 0;
}

