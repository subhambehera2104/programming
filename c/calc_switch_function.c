#include <stdio.h>
 
int sum(int x,int y)
{
	return x+y;
}

int sub(int x,int y)
{
	return x-y;
}
int mul(int x,int y)
{
	return x*y;
}
int div(int x,int y)
{
	return x/y;
}
int rem(int x,int y)
{
	return x%y;
}

 int main()
 {
 	int x,y;
	char choice;
 	printf("Enter number choice 1-5 for \n 1.sum \n 2.sub \n 3.mul \n 4.div \n 5.rem \n");
	scanf("%c",&choice);

 	printf("Enter number x ");
 	scanf("%d",&x);
 	printf("Enter number y ");
 	scanf("%d",&y);

 	
 	switch (choice)
 	{
 		case '1':
 			printf("%d",sum(x,y));
 			break;
 		case '2':
 			printf("%d",sub(x,y));
 			break;
 		case '3':
 			printf("%d",mul(x,y));
 			break;
 		case '4':
 			printf("%d",div(x,y));
 			break;
 		case '5':
 			printf("%d",rem(x,y));
 			break;
 		default:
 			printf("invalid choice");
 			break;
 	}
 	return 0;
 }