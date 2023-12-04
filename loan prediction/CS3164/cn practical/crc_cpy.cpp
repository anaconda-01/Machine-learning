#include<iostream>
using namespace std;
int main()
{
    int size;
    cout<<"enter the size fo the frame\n";
    cin>>size;
    int frame[20];
    cout<<"enter the frame\n";
    for(int i=0;i<size;i++)
    {
        cin>>frame[i];
    }
    cout<<"enter the size of the generator\n";
     int generator[20];
    for(int i=0;i<size;i++)
    {
        cin>>generator[i];
    }
    int rs=size-1;
    cout<<"number of zeros to be appended is "<<rs<<endl;
    for(int i=size;i<size+rs;i++)
    {
        frame[i]=0;
    }
    int temp[20];
    for(int i=0;i<size+rs;i++)
    {
        temp[i]=frame[i];
    }
    //preforming division
    for(int i=0;i<size;i++)
    {
        int j=0;
        int k=i;
        
    }
   

    

}