#include <iostream>
#include <string.h>
using namespace std;
int main()

{
	char name[10];
	cout<<"Enter name ";
	cin>>name;
	cout<<"Hello "<<name << endl ;
	cout<<"2nd char is "<<name[1]<<"\n";
	cout<<"name length "<<strlen(name);
		return 0;
}