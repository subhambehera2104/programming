#include <iostream>
using namespace std;
class Calculator
{
private:
 int result; 
public:
	int result2;
	Calculator(){
		result = 0;
		result2 =10;
	}
	// ~Calculator();

 public :
 int add(int x, int y){
 	result = x+y;
 	return result;
 }
	
	int sub(int x , int y){
		result = x-y;
 	    return result;
	}
};
int main()
{
	
	int num1,num2,result;
	printf("Enter num1");
	scanf("%d",&num1);
	printf("Enter num2");
	scanf("%d",&num2);
	Calculator c =  Calculator();
	result=c.add(num1,num2);
	printf("sum is %d",result);
	printf("Accessing public member variable %d\n",c.result2 ); 
	// ideally member variables should be private, if you access c.result, 
	// then it would throw error
	return 0;
}