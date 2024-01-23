#include<iostream>
using namespace std;
class Sort
{
public:
	Sort(){

	}

	void swap(int &x, int &y)
	{
		int temp=x;
		x=y;
		y=temp;
	}

	void ascending(int num[], int n)
	{
		cout<<"ascending ";
		for (int i = 0; i < n; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				if (num[i]>num[j])
				{
					swap(num[i], num[j]);
				}
			}
			cout<<num[i]<<", ";
		}
	}

	void descending(int num[], int n)
	{
		cout<<"descending ";
		for (int i = 0; i < n; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				if (num[i]<num[j])
				{
					swap(num[i], num[j]);
				}
			}
			cout<<num[i]<<", ";
		}
	}

};
int main()
{
	int num[] = {1, 45, 23, 82, -4, -7};
	int n = sizeof(num)/sizeof(num[0]);
	Sort s = Sort();
	s.ascending(num, n);
	s.descending(num, n);
	return 0;
}