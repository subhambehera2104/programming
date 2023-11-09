#include <iostream>
using namespace std;
 
int sum(int x,int y)
{
	return x+y;
}
 int main()
 {
 	int x=2, y=3;
 	int result=sum(x,y);
 	cout<<"sum of "<<x <<" and "<<y<<" is "<<result;

 	return 0;
 }