#include <stdio.h>
 
int sum(int x,int y)
{
	return x+y;
}

int sub(int x,int y)
{
	return x-y;
}

 int main()
 {
 	int x=2, y=3;
 	int result=sum(x,y);
 	printf("sum of %d and %d is %d ", x,y,result);

 	return 0;
 }