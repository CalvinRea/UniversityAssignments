#include <bits/stdc++.h>
using namespace std;

int main(){

int height,width,apple_x,apple_y,temp_x,temp_y,num_snek;
cin>>width;
cin>>height;
cin>>apple_x;
cin>>apple_y;
cin>>num_snek;


vector<int>w(width);
vector<vector<int>>v(height,w);

v[apple_y][apple_x]=5;

for(int j=1;j<num_snek+1;j++){

for(int i=0;i<3;i++){
	cin>>temp_x;
	cin>>temp_y;
	v[temp_y][temp_x]=j;	
}

}

for(auto y:v){
	for(auto x:y){
		cout<<x<<" ";
	}
		cout<<"\n";
}



return 0;}
