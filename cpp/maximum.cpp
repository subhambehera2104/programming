#include <iostream>
using namespace  std;
 int main()
 {
 	int x,y;
 	cout<<"Enter x ";
    cin>>x;
    cout<<"Enter y ";
    cin>>y;
    if(x==y)
    {
    	cout<<"equal ";
    }
    else if (x>y)
    {
    	cout<<"Maximum is "<<x;
    }
    else{
    	cout<<"Maximum is "<<y;
    }
   
 	return 0;
}

