#include <iostream>
using namespace std;

int main() {
    int n, t , x = 0;
    bool vencedor = false;
    cin >> n;

    int passageiros[n] = {};

    for (int i = 0; i < n; i++) {
        cin >> t;
        passageiros[i] = t;
    }
    cin >> x;

    for (int i = 0; i < n; i++) {
        if (passageiros[i] == x) {
            vencedor = true;
            cout << "Número da poltrona do vencedor: " << i << endl;
            break;
        }
    }
    if (!vencedor) {
        cout << "Não há vencedor" << endl;
    }
    return 0;
}