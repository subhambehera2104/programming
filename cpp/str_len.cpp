#include<iostream>
using namespace std;
int main()
{
char name[50];
cout<<"Enter Name ";
cin>>name;
int count=0;
while(name[count] != '\0')
{
    count++;
}
cout<<"string length is "<< count;
 return 0;
}