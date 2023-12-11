#include<iostream>
#include<vector>

using namespace std;

void arrayOperations(){
	cout << "Array\n";
	int num1[] = {3,4,5,6}; // declaration and initialisation in same line
	int n1 = sizeof(num1)/sizeof(num1[0]);
	for(int i=0;i<n1;i++){
		cout<< num1[i] <<" ";
	}

	cout <<"\n-----------------\n";

	int n2 = 4;
	int num2[n2]; /// Declaration
	num2[0] = 5; // assigning value to array index
	num2[1] = 6;
	num2[2] = 15;
	num2[3] = 25;
	for(int i=0;i<n2;i++){
		cout<< num2[i] <<" ";
	}

	cout <<"\n-----------------\n";

	int n3 = 4;
	int num3[n3]; /// Declaration
	printf("Enter %d numbers \n", n3 );
	for(int i=0;i<n3;i++){
		cin>> num3[i];
	}

	for(int i=0;i<n3;i++){
		cout<< num3[i] <<" ";
	}


	
  cout <<"\n-----------------\n";



}


void vectorOperations(){
	cout << "Vector\n";

    vector<int> num1{3,4,5,6}; // declaration and initialisation in same line
	int n1 = num1.size();
	for(int i=0;i<n1;i++){
		cout<< num1[i] <<" ";
	}

	cout <<"\n-----------------\n";

	vector<int> num2; // Declaration has no size because vector size can be dynamic
	num2.push_back(5);  // assigning value to vector index
	num2.push_back(6); 
	num2.push_back(15); 
	num2.push_back(25); 
	int n2 = num2.size();
	for(int i=0;i<n2;i++){
		cout<< num2[i] <<" ";
	}

	cout <<"\n-----------------\n";

	vector<int> num3; // Declaration
	int n3 = 4, x ;
	printf("Enter %d numbers \n", n3 );
	for(int i=0;i<n3;i++){
		cin>> x ;
		num3.push_back(x);
	}

	for(int i=0;i<n3;i++){
		cout<< num3[i] <<" ";
	}


	
  cout <<"\n-----------------\n";
}

int main()
{
	arrayOperations();
	vectorOperations();
}