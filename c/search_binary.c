#include<stdio.h>
int binarySearch(int arr[], int low, int high, int search)
{

	if (high>=low)
	{
		int mid=(low+high)/2;

		if (search==arr[mid])
		{
			return mid;
		}
		else if (search < arr[mid])
		{
			return(binarySearch(arr, low, mid-1, search));
		}
		else
		{
			return(binarySearch(arr, mid+1, high, search));
		}
	}else{
	 	return -1;
	}
}
int main()
{
	int arr[] ={1, 5, 6, 7, 8, 9};
	int search=6;
	int n =sizeof(arr)/sizeof(arr[0]);
	int result = binarySearch(arr, 0, n-1, search );
	if (result != -1)
	{
		printf("Element found at index %d ", result);
	}
	else
	{
		printf("Element not found ");
	}

	return 0;
}