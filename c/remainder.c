#include <stdio.h>
 int main()
 {
 	int x,y,remainder;
 	printf("Enter x ");
 	scanf("%d",&x);
 	printf("Enter y ");
 	scanf("%d",&y);
    remainder=x % y;
    printf("remainder is %d ",remainder);
 	return 0;
 }