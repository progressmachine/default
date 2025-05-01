#include <iostream>

namespace first {
    int x = 1;
}

namespace second {
    int x = 2;
}

void display() {
    int x = 0;
    using namespace second;
    std::cout << x << std::endl;
}

void display2() {
    using namespace second;
    std::cout << x << std::endl;
}

int main() {
    int x = 0;

    std::cout << x << std::endl;
    std::cout << first::x << std::endl;

    using namespace second;
    std::cout << x << std::endl; // gives 0

    display();
    display2();
}