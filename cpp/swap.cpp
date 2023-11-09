#include <iostream>
using namespace std;

void swap1(int x,int y)
{
	int temp = y;
	y = x;
	x = temp;
 }
 void swap2(int x,int y)
 {
	int z=x+y;
	y=z-y;
	x=z-x;
 }	
int main()
{
	int x =2;
	int y =3;

	swap1(x,y);
	cout<<"x is "<< x <<"\n";
    cout<<"y is "<< y <<"\n";


	x =2;
	y =3;
	swap2(x,y);
	cout<<"x is "<< x <<"\n";
    cout<<"y is "<< y <<"\n";

	return 0;
}