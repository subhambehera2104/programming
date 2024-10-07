#include<iostream>
using namespace std;

class Stack{
    int topIndex;
    int maximumSize;
    int* stack;

    public:
    Stack(int maxSize = 5){
        maximumSize = maxSize;
        stack= new int[maximumSize];
        topIndex = -1;   
    }

    void push(int elemnt){
        if(topIndex < maximumSize -1){
            stack[++topIndex]=elemnt;
        }
        else{
            cout<<"Stack is full";
        }
    }
    void top(){
        if(topIndex >= 0){
            cout << "Top element is : "<< stack[topIndex] << endl;
        }
        else{
            cout << "Stack is empty!" << endl;
        }
    }
    void pop(){
        if(topIndex >= 0){
            cout << "Removed element is : " << stack[topIndex--]<< endl;
        }
        else{
             cout << "Stack is empty!" << endl;
        }
    }
    };

int main(){
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.top();
    s.pop();
    s.top();
    return 0;
}