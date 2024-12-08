#include <iostream>
using namespace std;

int main() {
    int n, x, tot = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        tot += x;
    }
    cout << tot << endl;
    return 0;
}