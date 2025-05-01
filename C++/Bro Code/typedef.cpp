#include <iostream>

typedef std::string text_t; // the _t is convention for indicating a typedef
typedef int number_t; // text_t and number_t are aliases.

// using is more popular than typedef these days because it's more suitable with templates.

using text1_t = std::string;
using number1_t = int;

int main() {
    text_t name = "Bro";
    std::cout << name << "\n";

    number_t age = 18;
    std::cout << age << "\n";

    text1_t help = "Help";
    std::cout << help << "\n";

    number1_t num = 101;
    std::cout << num << "\n";
}