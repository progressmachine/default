// Include standard input-output stream
#include <iostream>

// Use standard namespace
using namespace std;

// Define class height
class height {
    int ft, in; // feet and inches

public:
    // Default constructor initializes feet and inches to 0
    height() { ft = 0; in = 0; }

    // Parameterized constructor to initialize feet and inches
    height(int a, int b) { ft = a; in = b; }

    // Setter function to get height from user
    void setter() {
        cout << "Enter height in feet and inches: ";
        cin >> ft >> in;
    }

    // Display function to print height in format f't"
    void display() {
        cout << ft << "'" << in << "\"" << endl;
    }

    // Function to add another height object to current object
    void sum(height x);
};

// Define sum function outside class
void height::sum(height x) {
    ft = ft + x.ft; // Add feet
    in = in + x.in; // Add inches

    // Convert excess inches to feet if inches >= 12
    if (in >= 12) {
        ft++;
        in -= 12;
    }
}

// Main function
int main() {
    height h1, h2(3, 7), h3; // Declare objects
    h1.setter();            // Get input for h1
    h1.display();           // Display h1
    h2.display();           // Display h2
    h2.sum(h2);             // Add h2 to itself
    h2.display();           // Display updated h2
}
