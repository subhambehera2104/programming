#include <iostream>
using namespace  std;

int main()
{
	int num,remainder;
	cout<<"Enter Number ";
	cin>>num;
	remainder=num%2;
	if (remainder==0)
	{
	cout<<num<<" is even";
	}
	 else
	{
    cout<<num<<" is odd";
	}
	return 0;
}
