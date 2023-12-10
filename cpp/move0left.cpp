#include<iostream>
using namespace std;
int main()
{
int arr[]={0, 1, 0, 0, 1};
int n=sizeof(arr)/sizeof(arr[0]);

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
    cout<<arr[j];
}

for(int k=countZero; k<n; k++)
{
    arr[k]=1;
    cout<<arr[k];
 }
 
return 0 ;	
}