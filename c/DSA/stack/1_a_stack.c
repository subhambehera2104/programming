#include<stdio.h>
#define MAXSIZE = 10;
struct stack{
    int maxSize = MAXSIZE;
    int *stack;
    int topIndex = -1;
} s1;

void push(stack, int element){
    if(topIndex == maxSize -1){
        printf("Stack is full");
    }
    else{
        s1 -> stack[++topIndex]=element;
    }
}
int main(){
    
}