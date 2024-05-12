#include <bits/stdc++.h>
using namespace std;

void print_vals(vector<array<int,2>> vals){
for(auto x:vals){
cout<<x[0]<<" , "<<x[1]<<endl;}
cout<<"\n";
}

int main(){

int height,width,apple_x,apple_y,temp_x,temp_y,num_snek,head_x,head_y;
int du=-height,dd=-height,dl=-width,dr=-width;

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
	if(j==1 and i==0){
		head_x=temp_x;
		head_y=temp_y;
	}	
}

}

int x_dist=apple_x-head_x;
int y_dist=apple_y-head_y;

vector<string> n={"DOWN","LEFT","RIGHT","UP"};
vector<array<int,2>> vals={{0,0},{0,1},{0,2},{0,3}};//value,index to corresponding v above

if(y_dist>0){
vals[0][0]++;
}else{vals[3][0]++;}

if(x_dist>0){
vals[2][0]++;
}else{vals[1][0]++;}

if(abs(x_dist)>abs(y_dist)){

vals[1][0]++;
vals[2][0]++;

}else if(abs(x_dist)<abs(y_dist)){

vals[0][0]++; 
vals[3][0]++;

}

if(head_y<height-1){
	if(!(v[head_y+1][head_x]==0 or v[head_y+1][head_x]==5)){
		vals[0][0]=-1;	
	}
}else{vals[0][0]=-1;}
if(head_x>0){
	if(!(v[head_y][head_x-1]==0 or v[head_y][head_x-1]==5)){
			vals[1][0]=-1;
	}
}else{vals[1][0]=-1;}
if(head_x<width-1){
	if(!(v[head_y][head_x+1]==0 or v[head_y][head_x+1]==5)){
			vals[2][0]=-1;
	}
}else{vals[2][0]=-1;}
if(head_y>0){
	if(!(v[head_y-1][head_x]==0 or v[head_y-1][head_x]==5)){
			vals[3][0]=-1;
	}
}else{vals[3][0]=-1;}


array<int,2>temp;
for(int i=0;i<4-1;i++){
for(int j=0;j<4-1;j++){
	
	if(vals[j][0]>vals[j+1][0]){
	temp=vals[j+1];
	vals[j+1]=vals[j];
	vals[j]=temp;
	}
}

}


if(vals[3][0]>-1){
if(vals[3][0]==vals[3-1][0]){
	if(vals[3][1]<vals[3-1][1]){
	cout<<n[vals[3][1]]<<endl;
	cout<<n[vals[3-1][1]];
	}else{
	cout<<n[vals[3-1][1]]<<endl;
	cout<<n[vals[3-1][1]];
	}
}else{
cout<<n[vals[3][1]]<<endl;
}
}

return 0;}
