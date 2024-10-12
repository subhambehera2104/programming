//string reverse program using library
#include <iostream>
#include <stack>
using namespace std;

stack<char>s;
void push(char element){
    s.push(element);
}
void pop(char element){
    for (int i = 0; i<s.size(); i++){
        if (s.size()>0){
            cout<<s.top();
        }
    }
}

int main(){
    char element;
    cout<< "Enter name or number";
    cin>> element;
    push(element);
    pop(element); 
}