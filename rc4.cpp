#include <iostream>

using namespace std;

int T[256];// un vector temporar pentru generarea streamului
int S[256];//stream-ul pe care il vom folosi
static string key = "key";//cheia pe care o vom folosi
static string text = "Plaintext";//Textul de encriptat
string enc;
int KSA(){  //Key-Scheduling Algorithm
    for(int i = 0; i<255; i++){
        T[i]=i;
    }
    int j = 0;
    int c;
    int keyk[256];
    for (int i = 0; i<key.length();i++){
        keyk[i]=int(key[i]);
    }
    for(int i = 0; i<255; i++){
        j = (j + T[i] + keyk[i % key.length()]) % 256;
        c =T[i];
        T[i] = T[j];
        T[j] = c;
    }
    return 0;
}

int PRGA(){ //Pseudo random generation algorithm
    int i = 0;
    int j = 0;
    int c;
    int counter = 0;
    while (counter <= text.length()){   // Folosim lungimea textului de ecriptata ca sa stim cat stream trebuie sa generam
        i = (i+1)%256;
        j = (j+T[i])%256;
        c =T[i];
        T[i] = T[j];
        T[j] = c;
        S[counter]=T[(T[i] + T[j]) % 256];
        counter++;
    }
    return 0;
}
int main(){
    KSA();
    PRGA();
    for(int i=0;i<text.length();i++){
        enc[i]=char(int(text[i])^S[i]);
            cout<<char(int(text[i])^S[i]);  //XOR
    }
    cout<<endl;

}
