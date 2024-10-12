//stack usign stack library
//push() -> it can pus automaticly into stack
//pop() -> can pop from stack
//top() -> It can give answer of the top element of stack
//empty() -> it will check the stack is empty or no

#include <iostream>
#include <stack> //This is library of stack
using namespace std;
int main(){
    stack<int> s; //create a stack of integers with out using class

    //Push element into stack
    s.push(1);
    s.push(2);
    s.push(3);
    //print the size of stack
    cout << "Your stack size is : " << s.size() << endl;
    //print the top element of stack
    cout << "Top element is : " << s.top() << endl;

    //remove the top element
    s.pop();

    //print the top element after pop
    cout << "Top element after pop is : " << s.top() << endl;


    return 0;
}