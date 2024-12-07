#include <iostream>
using namespace std;

int main() {
    int n;

    do {
        cin >> n;
        if (n != 0) {
            cout << (n * -1) << endl;
        }
    } while (n != 0);

    return 0;
}