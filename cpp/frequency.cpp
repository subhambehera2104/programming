#include<iostream>
#include<map>
#include<unordered_map>
using namespace std;

void frequencyNum(int num[], int n, int frequency[])
{
   
    for(int i=0; i<n; i++)
    {
        frequency[i]=1;
    }
    for(int i =0; i<n; i++)
    {
        if(frequency[i]==-1)
        {
            continue;
        }
        for(int j = i+1; j<n; j++)
        {
            if(num[i]==num[j])
            {
                frequency[i]++;
                frequency[j]=-1;
            }
        }
    }
}


void frequencyBest(int num[], int n)
{
    unordered_map<int,int> frequencyMap;
    for(int i =0; i< n; i++)
    {
        if (frequencyMap.find(num[i]) == frequencyMap.end())
        {
           frequencyMap[num[i]]=1;
        }
        else
        {
             frequencyMap[num[i]]++;
            
        }
    }

      for (auto &iterator: frequencyMap)
    {
       cout<<"key "<< iterator.first << "value "<< iterator.second << "\n";
    }
    
}

int main()
{
    int num[] = {1, 4, 2, 0, 1, 4};
    int n = sizeof(num)/sizeof(num[0]);
    int res[n];
    
    frequencyNum(num, n, res);
    for(int i = 0; i<n; i++)
    {
        if(res[i]!=-1)
        {
            cout<<"key " <<num[i] << "value "<<res[i]<<"\n";
        }
    }

    cout<< "---------------\n";
   
    frequencyBest(num, n);
  
    return 0;
}