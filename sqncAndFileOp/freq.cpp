#include<iostream>
using namespace std;

int main(){
    string s="";
    cout << "Enter a string :: "; //abcdefgabc
    cin >> s;
    int l = s.length();
    bool visited[l] = {false};

    for(int i=0; i<=l; i++){
        if(visited[i])
            continue;
        int count = 1;
        for(int j=i+1; j<=l; j++){
            if(s[i]==s[j]){
                count++;
                visited[j]=true;
            }
        }
        cout << s[i] << " : " << count << endl;
    }
    return 0;
}