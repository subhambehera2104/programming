#include<stdio.h>
int checkprime(int num){
    int isPrime  =1;
    if(num==1)
    {
        printf("Neither prime nor composite");
    }
    else
    {
        for(int i = 2; i<=num/2; i++){
            if(num %i==0)
                {
                    isPrime=0;
                    break;
                }
         }
                
    }

    return isPrime;
}

void primeNumbers(int k)
{
    printf("prime numbers ");
    int isPrime = 1;
    for(int i =2; i<k; i++)
    {
        isPrime = checkprime(i);
        if (isPrime == 1){
            printf("%d ,",i);
        }
       
    }
}   
int main()
{
    int num, k ;
    int isPrime=1;
    printf("Enter number ");
    scanf("%d",&num);
    printf("isPrime %d\n",checkprime(num));

    printf("Enter k which will display prime numbers until k ");
    scanf("%d",&k);
    primeNumbers(k);
    
   
}