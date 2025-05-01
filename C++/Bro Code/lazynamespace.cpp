#include <iostream>

void another() {
    using std::cout;
    using std::string;

    // safer than using namespace std;

    string name = "Bro";
    cout << "Hello " << name << std::endl;
}

int main() {
    using namespace std;

    string name = "Bro";
    cout << "Hello " << name << endl;

    another();
    
    return 0;
}