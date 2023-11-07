#include <iostream>
#include<cctype>
using namespace  std;
 int main()
 {
 	char c, ch;
 	cout<<"Enter Character ";
 	cin>>c;

 	ch = tolower(c);

	if (ch == 'a' || ch == 'e'  || ch == 'i' || ch == 'o' || ch == 'u')
	{
		cout<<c << " is vowel";
	}
	else
	{
		cout<<c << "is Consonant";
	
	}
 	
 	return 0;
 }