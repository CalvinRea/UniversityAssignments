#include <bits/stdc++.h>
using namespace std;

int main(){

int height,width,apple_x,apple_y,temp_x,temp_y,temp_x2,temp_y2,num_snek,body_len;
cin>>width;
cin>>height;
cin>>apple_x;
cin>>apple_y;
cin>>num_snek;


vector<int>w(width);
vector<vector<int>>v(height,w);

v[apple_y][apple_x]=5;

for(int j=1;j<num_snek+1;j++){
cin>>body_len;
cin>>temp_x;
cin>>temp_y;
for(int i=1;i<body_len;i++){
	
	cin>>temp_x2;
	cin>>temp_y2;
	
	if(temp_y<temp_y2){
	
	for(int counter=temp_y;counter<=temp_y2;counter++){
		v[counter][temp_x]=j;
	}
	
	}else if(temp_y>temp_y2){
	
	for(int counter=temp_y2;counter<=temp_y;counter++){
		v[counter][temp_x]=j;
	}
	
	}else if(temp_x<temp_x2){
	
	for(int counter=temp_x;counter<=temp_x2;counter++){
		v[temp_y][counter]=j;
	}
	
	}else if(temp_x>temp_x2){
	
	for(int counter=temp_x2;counter<=temp_x;counter++){
		v[temp_y][counter]=j;
	}
	
	}
temp_x=temp_x2;
temp_y=temp_y2;
	
}



}

for(auto y:v){
	for(auto x:y){
		cout<<x<<" ";
	}
		cout<<"\n";
}



return 0;}
