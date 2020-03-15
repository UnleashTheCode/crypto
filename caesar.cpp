
#include <iostream>
using namespace std;

int main(){
    string c;
    char n[50];
    int k;
    cout << "Enter a message to be encrypted: ";
    getline(cin, c);
    cout << "Enter Key: ";
    cin >> k;
    for (int i; i < c.size();i++){
        if (c[i] != ' '){
        n[i] = char(int(c[i]) + k);
        }
        else{
            n[i] += ' ';
        }
    }
    cout << "Encrypted message: " << n;
    return 0;
}