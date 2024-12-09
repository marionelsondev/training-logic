#include <iostream>

int main() {
    int n, x, toto = 0;
    std::cin >> n;
    int e[n] = {};
    for (int i = 0; i < n; i++) {
        std::cin >> e[i];
    }
    std::cin >> x;
    for (int i = 0; i < n; i++) {
        if (e[i] == x) {
            toto += 1;
        }
    }
    std::cout << toto << std::endl;
    return 0;
}