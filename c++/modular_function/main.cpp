#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    if (n >= 0) {
        cout << n << endl;
    }

    if (n < 0) {
        cout << (n * -1) << endl;
    }
    return 0;
}