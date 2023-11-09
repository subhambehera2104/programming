#include <stdio.h>
#include <string.h>
int main()
{
	char name[10];
	printf("Enter name ");
	scanf("%s", name);
	printf("Hello %s \n",name);
	printf("2nd char %c \n",name[1]);
	printf("name length %d", strlen(name));
		return 0;
}