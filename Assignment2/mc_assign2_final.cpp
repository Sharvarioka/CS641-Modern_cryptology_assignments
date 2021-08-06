#include<iostream>
#include<algorithm>
#include<string>
#include<bits/stdc++.h>
using namespace std;

string removeDuplicates(string str) 
{ 
    
   int ind = 0; 
   int n=str.size();  
   for (int i=0; i<n; i++) { 
   		if(str[i]!=' ')  
   		{	
			int j;   
			for (j=0; j<i; j++)  
	        	if (str[i] == str[j]) 
	           		break; 
	     if (j == i) 
	        str[ind++] = str[i]; 
		}
   } 
   str.resize(ind); 
   return str; 
}

char next(int i, char alpha, string key)
{
	int flag=0;
	for(int j=0;j<i;j++)
	{
		if(alpha==key[j] || alpha=='J')
		{
			return next(i,alpha+1,key);
			flag=1;
		}
	}
	if(flag==0)
	{
	return alpha;
	}			
}

void find(char mat[5][5],char c,int pos[2])
{
	if(c=='J')
	{
		c='I';
	}
	for(int i=0;i<5;i++)
 	{
 		for(int j=0;j<5;j++)
		{
			if(c==mat[i][j])
			{
			pos[0]=i;
			pos[1]=j;
			}
		}
	}
}



int main()
{
string cipher="TR XYCB MH AFC MUVY EOHPTCS, AFCSS TE QCSI NTYIMS TNA AFCSC. EMRBH XAA VAFR MIUCQPUH 'LMRL_CCETOT' FN HM AKUXAHK. OTA WANA OTXT FFU EISCWNAF HME BFU MCVA UGTOTRE. BM HYLF IFU UVTY ANE HBSEI QYOQM OUVSF AM EAFTE PYHYS XNSKE IFUSC.";
 
string original=cipher;
for(int i=0;i<cipher.length();i++)
{
	if((isalpha(original[i])))
		{	
			original[i]=toupper(cipher[i]);
		}
	else
	original[i]=cipher[i];
	
}

char mat[5][5]= { NULL };
string key;
int k=0;
char alpha=64;

cout<< "enter key" <<endl;
getline(cin,key);

key=removeDuplicates(key);
for(int j=0;j<key.length();j++)
{
	key[j]=toupper(key[j]);
}
 for(int i=0;i<5;i++)
 {
 	for(int j=0;j<5;j++)
	{
		while(!mat[i][j])
		{
			if(k<key.length())
			{
				int flag=0;
				for(int l=0;l<k;l++)
				{
					if(key[k]==key[l])
					flag=1;
				}
				if(flag==0)
				{	
				mat[i][j]=key[k];
				k++;
				}
				else
				k++;
			}
			
			else
			{
				alpha = next(key.length(), alpha+1,key);
				mat[i][j]= alpha;
			}
		}
	}
}			
cout<<endl<<endl;
for (int i = 0; i < 5; i++) 
{ 
   for (int j = 0; j < 5; j++) 
   { 
      cout << mat[i][j] << " "; 
   } 
     
   // Newline for new row 
   cout << endl; 
}

int total=0;
for(int i=0;i<original.length();i++)
{
	if((isalpha(original[i])))
		{	
			//cout << original[i];
			total++;
		}
}
cout << endl;
cout <<"Ciphertext: "<< cipher<<endl;
cout << endl;

int j=0,p=0,pos2[2],pos1[2];
char f,s;
for(int i=0;i<total/2;i++)
{
	while(!(isalpha(original[j])))
		{	
			j++;
		}
	f=original[j];
	find(mat,f,pos1);
	p=j;
	j=j+1;
	while(!(isalpha(original[j])))
		{	
			j++;
		}
	s=original[j];
	find(mat,s,pos2);
	if(pos1[0]==pos2[0])
		{
			if(pos1[1]==0)
			{
				pos1[1]=4;
				pos2[1]=pos2[1]-1;
			}
			else if(pos2[1]==0)
			{
				pos2[1]=4;
				pos1[1]=pos1[1]-1;
			}
			else
			{
			pos1[1]=pos1[1]-1;
			pos2[1]=pos2[1]-1;
			}
			if(islower(cipher[p])) 
			original[p]=tolower(mat[pos1[0]][pos1[1]]);
			else				
			original[p]=mat[pos1[0]][pos1[1]];
			
			if(islower(cipher[j]))
			original[j]=tolower(mat[pos2[0]][pos2[1]]);
			else
			original[j]=mat[pos2[0]][pos2[1]];
		}
	else if(pos1[1]==pos2[1])
		{
			if(pos1[0]==0)
			{
				pos1[0]=4;
				pos2[0]=pos2[0]-1;
			}
			else if(pos2[0]==0)
			{
				pos2[0]=4;
				pos1[0]=pos1[0]-1;
			}
			else
			{
			pos1[0]=pos1[0]-1;
			pos2[0]=pos2[0]-1;
			}
			if(islower(cipher[p]))
			original[p]=tolower(mat[pos1[0]][pos1[1]]);
			else
			original[p]=mat[pos1[0]][pos1[1]];
			
			if(islower(cipher[j]))
			original[j]=tolower(mat[pos2[0]][pos2[1]]);
			else
			original[j]=mat[pos2[0]][pos2[1]];
		}
	else
		{
			if(islower(cipher[p]))
			original[p]=tolower(mat[pos1[0]][pos2[1]]);
			else
			original[p]=mat[pos1[0]][pos2[1]];
			
			if(islower(cipher[j]))
			original[j]=tolower(mat[pos2[0]][pos1[1]]);
			else
			original[j]=mat[pos2[0]][pos1[1]];
		}
	j=j+1;	
}
cout << "Plaintext: "<<original<<endl;
}


