#include <iostream>
using namespace std;

int main() {
    char z, g, d, c;

    cin >> z >> g;
    cin >> d >> c;

    if (d == z) {
        cout << "Bloqueado" << endl;
    } else {
        cout << "Driblado" << endl;
        if (c == g) {
            cout << "...e o goleiro pega" << endl;
        } else {
            cout << "Gol" << endl;
        }
    }
    return 0;
}