#include <iostream>

int main(){
    std::cout << "I like pizza." << "\n"; // \n is better that std::endl performance-wise.
    std::cout << "It's really good." << std::endl; // std::endl will flush the output-buffer, that is its advantage.
    return 0;
}