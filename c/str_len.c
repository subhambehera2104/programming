#include<stdio.h>
int main()
{
char name[50];
printf("Enter Name ");
scanf("%s",name);
int count=0;
while(name[count] != '\0')
{
    count++;
}
printf("string length is %d ",count);
 return 0;
}