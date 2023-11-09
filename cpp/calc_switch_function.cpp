#include <iostream>
using namespace std;
 
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
int divide(int x,int y)
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
 	cout<<"Enter number choice 1-5 for \n 1.sum \n 2.sub \n 3.mul \n 4.div \n 5.rem \n";
	cin>>choice;

 	cout<<"Enter number x ";
 	cin>>x;
 	cout<<"Enter number y ";
 	cin>>y;

 	switch (choice)
 	{
 		case '1':
 			cout<<sum(x,y);
 			break;
 		case '2':
 			cout<<sub(x,y);
 			break;
 		case '3':
 			cout<<mul(x,y);
 			break;
 		case '4':
 			cout<<divide(x,y);
 			break;
 		case '5':
 			cout<<rem(x,y);
 			break;
 		default:
 			cout<<"invalid choice";
 			break;
 	}

 	
 	
 	return 0;
 }