//  TCS ques
// N Employess play game for N<=10
// how many ways to form Pairs or Single if odd then 1 way
// if even the pair multiple gap 
#include<iostream>
using namespace std;

int NC2(int N){
	return N*(N-1)/2;
}

int main(){

int N;
cin>>N;

if(N<=10){
if(N%2!=0){
	cout<<1;
}
else if(N%2==0){

// n + nc2

cout<<(N+NC2(N));
}
}
return 0;
}