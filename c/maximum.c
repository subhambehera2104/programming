#include <stdio.h>
int main()
{
	int x,y;
	printf("Enter x ");
	scanf("%d",&x);
	printf("Enter y ");
	scanf("%d",&y);
	if (x==y)
	{
		printf("equal %d ", x);
	}
    else if(x>y){
		printf("maximum is %d",x);

	}
	else{
		printf("maximum is %d",y);
    }

return 0;
}
