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
 s1 = stack();
 s1->push(3);
 s1->push(2);
 s1->push(3);   
}