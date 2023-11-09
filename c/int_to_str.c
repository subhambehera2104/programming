#include <stdio.h>
#include <string.h>
int main()
{
	int num = 452;
	char res[3];

	sprintf(res,"%d",num);
	printf("%s \n",res );
	printf("string len %d \n",strlen(res));
	printf("string 2nd char %c", res[1]);

	return 0;
}