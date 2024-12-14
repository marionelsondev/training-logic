#include <iostream>
#include <vector>

int main() {
    int n = 0;
    std::cin >> n;
    std::vector<int> f(n);

    for (int i = 0; i < n; i++) {
        std::cin >> f[i];
    }
    for (int i = n - 1; i >= 0; i--) {
        std::cout << i + 1 << ": " << f[i] << std::endl;
    }
    return 0;
}