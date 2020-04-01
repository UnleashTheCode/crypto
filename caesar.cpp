
#include <iostream>
using namespace std;

int main(){
    string c;
    char n[50];
    int k;
    char mod;
    cout << "What do you want to do enc(e)/dec(d): ";
    cin >> mod;
    if (mod == 'e'){
        cout << "Enter a message to be encrypted: ";
        cin.ignore();
        getline(cin, c);
        cout << "Enter Key: ";
        cin >> k;
        for (int i=0; i < c.size();i++){
            if (c[i] != ' '){
                n[i] = char(int(c[i]) + k); // transformam caracterul in cod ASCII, rezultatul il adunam cu cheia si il transformam inapoi in caracter
            }
            else{
                n[i] += ' ';     // In caz ca este spatiu il lasam neschimbat (in caz ca vrem sa encriptam si spatiul scoatem if-ul
            }
    }
    cout << "Encrypted message: " << n << endl;
    }
    else{
        cout << "Enter a message to be decrypted: ";
        cin.ignore();
        getline(cin, c);
        cout << "Enter Key: ";
        cin >> k;
        for (int i = 0; i < c.size();i++){
            if (c[i] != ' '){
                n[i] = char(int(c[i]) - k);// transformam caracterul in cod ASCII, rezultatul il scadem cu cheia si il transformam inapoi in caracter
            }
            else{
                n[i] += ' ';// In caz ca este spatiu il lasam neschimbat (in caz ca vrem sa encriptam si spatiul scoatem if-ul
            }
        }
        cout << "Decrypted message: " << n << endl;
    }
    return 0;
}
