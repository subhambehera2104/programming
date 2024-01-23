#include<iostream>
using namespace std;
class Student
{
private :
string name, roll, mobile;
public:
	Student(string name1, string roll1, string mobile1)
	{
		name=name1;
		roll=roll1;
		mobile=mobile1;
	}
	void display()
	{
		cout<<"name"<<name <<"\n" <<"roll"<<roll << "\n" <<"mobile"<<mobile <<"\n";
	}
};
int main()
{


	Student s1=Student("xyz", "123", "1234567890");
	s1.display();

  	string name, roll, mobile;
	cout<<"Enter Student name ";
	cin>>name;
	cout<<"Enter Student roll ";
	cin>>roll;
	cout<<"Enter Student mobile number ";
	cin>>mobile;

	Student s2=Student(name, roll, mobile);
	s2.display();
	return 0;
}