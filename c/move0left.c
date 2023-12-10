#include<stdio.h>

int* move0toleft1(int arr[], int n){
    int countZero=0;

    for(int i=0; i<n; i++)
    {
        if(arr[i]==0)
        {
            countZero++;
        }

    }
        
    for(int j=0; j<countZero; j++)
    {
        arr[j]=0;
        
    }

    for(int k=countZero; k<n; k++)
    {
        arr[k]=1;
        
    }
    return arr;
}

int* move0toleft2(int arr[], int n)
{
    int type0Index =0;
    int type1Index =n-1;
    while(type0Index <type1Index)
    {
        if (type0Index==1)
        {
            while(type1Index !=0)
            {
                int temp = type0Index;
                  arr[type0Index ] = arr[type0Index ];
                  arr[type1Index] = temp;
                  type0Index--;
            }
        }
        else
           {
             type1Index++;
           } 
        
    }
    
   return arr;
}

int main()
{
int arr[]={0, 1, 0, 0, 1};
int n=sizeof(arr)/sizeof(arr[0]);

int* result= move0toleft1(arr,n);
for(int i = 0; i<n; i++){
    printf("%d", result[i]);
}
printf("\n");
int* result2= move0toleft2(arr,n);
for(int i = 0; i<n; i++){
    printf("%d", result[i]);
}

return 0 ;	
}