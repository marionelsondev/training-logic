#include <iostream>
#include <vector>

int main() {
    int t, n, sum_dps = 0;
    std::cin >> t >> n;
    std::vector<int> x(n);

    t = 28000 / t;
    
    for (int i = 0; i < n; i++) {
        std::cin >> x[i];
        sum_dps += x[i];
    }

    if (sum_dps >= t) {
        std::cout << "Macacos venceram!" << std::endl;
    } else {
        std::cout << "O BAD venceu!" << std::endl;
    }

    return 0;
}