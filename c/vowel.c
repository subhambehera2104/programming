#include <stdio.h>
#include<ctype.h>
int main()
{
	char ch;
	printf("Enter character ");
	scanf("%c",&ch);
	ch = tolower(ch);
	if (ch == 'a' || ch == 'e'  || ch == 'i' || ch == 'o' || ch == 'u')
	{
		printf("%c is vowel",ch);
	}
	else
	{
		printf("%c is Consonant",ch);
	}
	return 0;
}