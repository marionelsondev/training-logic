#include <iostream>
#include <vector>

int main() {
    int n, p = 0;
    std::cin >> n >> p;
    std::vector<int> x(p);

    if (p > 0) {
        for (int i = 0; i < p; i++) {
            std::cin >> x[i];
        }
    }

    for (int i = 1; i <= n; i++) {
        bool found = false;
        for (int seat_occupied : x) {
            if (i == seat_occupied) {
                found = true;
                break;
            }
        }

        if (!found) {
            std::cout << i << ' ';
        }
    }

    return 0;
}