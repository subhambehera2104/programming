#include <stdio.h>
void swap1(int &x,int &y)
	int temp = y;
	y = x
	x = temp
 
 void swap2(int &x,int &y)
	int z=x+y;
	y=z-y
	x=z-x
	
int main()
{
	int x =2;
	int y =3;
	swap1(x,y)
		printf("%d",x);
	    printf("%d",x);
	int x =2;
	int y =3;
	swap2(x,y)
		printf("%d",x);
	    printf("%d",x);

	return 0;
}