// Include input-output stream
#include <iostream>

// Use standard namespace
using namespace std;

// Define height class
class height {
    int ft, in; // feet and inches

public:
    // Default constructor
    height() { ft = 0; in = 0; }

    // Parameterized constructor
    height(int a, int b) { ft = a; in = b; }

    // Setter function for input
    void setter() {
        cout << "Enter height in feet and inches: ";
        cin >> ft >> in;
    }

    // Display height in ft'in"
    void display() {
        cout << ft << "'" << in << "\"" << endl;
    }

    // Function to subtract another height
    void subtract(height);
};

// Define subtract function outside class
void height::subtract(height x) {
    ft = ft - x.ft;  // Subtract feet
    in = in - x.in;  // Subtract inches

    // If inches become negative, adjust by borrowing 1 foot
    if (in < 0) {
        ft--;
        in += 12;
    }
}

// Main function
int main() {
    height h1, h2(3, 7), h3;  // Declare objects
    h1.setter();             // Input for h1
    h1.display();            // Display h1
    h2.display();            // Display h2
    h2.subtract(h2);         // Subtract h2 from itself
    h2.display();            // Display result
}
