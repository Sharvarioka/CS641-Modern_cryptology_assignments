#include<iostream>
#include<algorithm>
#include<string>
#include<bits/stdc++.h>
using namespace std;

bool cmp(pair<char, float>& a, 
         pair<char, float>& b) 
{ 
    return a.second > b.second; 
} 

vector<pair<char,float>> sorting(map<char, float>& M) 
{ 
    vector<pair<char, float> > A; 

    for (auto& it : M) { 
        A.push_back(it); 
    } 
  
    sort(A.begin(), A.end(), cmp); 
  	return A;
   
} 

int main()
{
string original="wsam ie pjo ysgtm eyipbya .P axg niphay y, mey syw ahgm ewhrg tw hmysyam wh meyiepjo ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy whmy sy amwh rmephmewagh y!Me yigu ynay utg smew ajya apr ywap awjfkya no a mwmnmw ghiwfeyswhve wieuwr wm aepby oyyhae wtmy uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd dvwmegnmmey dngmya. Mew awameyt";
map<char,float>m;
map<char ,float> ::iterator itr;
int non_alpha=0;
vector<pair<char, float> > A; 

string decrypted_msg;
decrypted_msg=original;
for(int i=0;i<original.length();i++)
{
	if(!(isalpha(original[i])))
		{	non_alpha++;
			continue;
		}
	else
	{
		m[tolower(original[i])]++;
	}
}
int sum=0;

for(itr=m.begin();itr!=m.end();itr++)
{
	
	sum+=itr->second;
}

for(itr=m.begin();itr!=m.end();itr++)
{
	
	m[itr->first]=(m[itr->first]*100)/sum;
		
}

A=sorting(m);

for (auto& it : A) 
{ 
  
	cout << it.first << ' '
	     << it.second << endl; 
}

cout<<endl<<endl;

// for(int i=0;i<original.length();i++)
// { 
// 	if(original[i]>= 'a' && original[i] <= 'z')
// 	{
// 	original[i]=original[i]-32;
// 	}
// }
	
cout<<"original: "<<original<<endl<<endl<<endl;;

int flag=0,exit=0;
char o,n;


	cout << "enter 0 to proceed and 1 to exit " << endl; 
	cin >> exit;
	while(exit!=1)
	{
	cout << "Replace" << endl; 
	cin >> o;
	n=n-32;
	cout << "With" << endl; 
	cin >> n;
	
	for(int i=0;i<original.length();i++)
	{ 
	 flag=0;
	 switch(tolower(o))
	 { 
	 	
		case 'y':
	    	{
	 	if(original[i]=='Y')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='y')	 {decrypted_msg[i]=tolower(n); flag=1;}

		break;
		}

		case 'm':
	   	{
		if(original[i]=='M')	 {decrypted_msg[i]=toupper(n); flag=1;} 
		if(original[i]=='m')	 {decrypted_msg[i]=tolower(n); flag=1;} 

		break;
		}

		case 'e':
		{
	 	if(original[i]=='E')	 {decrypted_msg[i]=toupper(n); flag=1;} 
	 	if(original[i]=='e')	 {decrypted_msg[i]=tolower(n); flag=1;} 

		break;
		}

		case 'p':
	    	{
		if(original[i]=='P')	 {decrypted_msg[i]=toupper(n); flag=1;}
		if(original[i]=='p')	 {decrypted_msg[i]=tolower(n); flag=1;} 

		break;
		}

		case 'w':
	    	{
	 	if(original[i]=='W')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='w')	 {decrypted_msg[i]=tolower(n); flag=1;}

		break;
		}

		case 'a':
	    	{
		if(original[i]=='A')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='a')	 {decrypted_msg[i]=tolower(n); flag=1;}
		break;
		}

		case 'j':
		{
		if(original[i]=='J')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='j')	 {decrypted_msg[i]=tolower(n); flag=1;}
		break;
		}

		case 'r':
	    {

		if(original[i]=='R')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='r')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}

		case 's':
	    {
	 	
		if(original[i]=='S')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='s')	 {decrypted_msg[i]=tolower(n); flag=1;}
		break;
		}

		case 't':
	    	{

		if(original[i]=='T')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='t')	 {decrypted_msg[i]=tolower(n); flag=1;}
		break;
		}

		case 'h':
	    	{

		if(original[i]=='H')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='h')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}

		case 'g':
	    	{

		if(original[i]=='G')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='g')	 {decrypted_msg[i]=tolower(n); flag=1;}
		break;
		}

		case 'i':
		{

		if(original[i]=='I')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='i')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}
		
		case 'o':
		{
	 	if(original[i]=='O')	 {decrypted_msg[i]=toupper(n); flag=1;} 
	 	if(original[i]=='o')	 {decrypted_msg[i]=tolower(n); flag=1;} 
		break;
		}

		case 'b':
		{

		if(original[i]=='B')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='b')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}

		case 'k':
		{

		if(original[i]=='K')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='k')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}


		case 'v':
		{ 

		if(original[i]=='V')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='v')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}

		case 'f':
		{

		if(original[i]=='F')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='f')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}

		case 'u':
		{

		if(original[i]=='U')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='u')	 {decrypted_msg[i]=tolower(n); flag=1;}
		break;
		}

		case 'n':
		{

		if(original[i]=='N')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='n')	 {decrypted_msg[i]=tolower(n); flag=1;}
		break;
		}

		case 'x':
		{

		if(original[i]=='X')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='x')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}

		case 'd':
		{

		if(original[i]=='D')	 {decrypted_msg[i]=toupper(n); flag=1;}
	 	if(original[i]=='d')	 {decrypted_msg[i]=tolower(n); flag=1;}		
	 	break;
		}
	 	default:
	 	{

			if (flag==0)
	  			decrypted_msg[i]=original[i];
	  	}
	  }
	}

  cout<<"original: "<<original<<endl<<endl<<endl;
  cout<<"decrypted :"<<decrypted_msg<<endl<<endl;
  cout << "enter 0 to proceed and 1 to exit " << endl; 
  cin >> exit;

}

cout<<"original: "<<original<<endl<<endl<<endl;
cout<<"decrypted :"<<decrypted_msg<<endl<<endl;
}


