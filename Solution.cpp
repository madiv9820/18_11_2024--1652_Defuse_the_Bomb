#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();  // Get the length of the code array
        vector<int> decrypted_Code(n, 0);  // Initialize the result array with zeros
        int nextKIndexSum = 0;  // This variable will store the sum of the next k elements (or previous |k| elements)

        // Case 1: When k > 0 (sum the next k elements)
        if(k > 0) {
            int left = 1, right = 1;  // Initialize left and right pointers to the first element after the current one

            // Sum the next k elements starting from the right pointer
            for(int i = 0; i < k; ++i) {
                nextKIndexSum += code[right];  // Add the element at the 'right' pointer to the sum
                right = (right + 1) % n;  // Move the 'right' pointer circularly (wraps around when it goes beyond n-1)
            }

            // Now slide the window for each index in the code array
            for(int index = 0; index < n; ++index) {
                decrypted_Code[index] = nextKIndexSum;  // Set the decrypted value at the current index

                // Slide the window:
                // 1. Remove the element at 'left' (the leftmost element in the window) from the sum
                nextKIndexSum -= code[left];
                left = (left + 1) % n;  // Move 'left' to the next position, wrapping around when it reaches n

                // 2. Add the element at 'right' (the next element to the right of the window) to the sum
                nextKIndexSum += code[right];
                right = (right + 1) % n;  // Move 'right' to the next position, wrapping around when it reaches n
            }
        }
        // Case 2: When k < 0 (sum the previous |k| elements)
        else if(k < 0) {
            int left = -1, right = -1;  // Initialize left and right to the last element (n-1)

            // Sum the previous |k| elements (use the absolute value of k)
            for(int i = 0; i < -k; ++i) {  // Iterate through |k| elements to sum them
                nextKIndexSum += code[n + left];  // Add the element at the 'left' pointer (adjusted for circular indexing)
                left = left - 1;  // Move 'left' to the previous position
            }

            // Now slide the window for each index in the code array
            for(int index = 0; index < n; ++index) {
                decrypted_Code[index] = nextKIndexSum;  // Set the decrypted value at the current index

                // Slide the window:
                // 1. Move 'left' to the next position
                left += 1;
                // 2. Remove the element at 'left' from the sum and adjust 'left' for the circular array
                nextKIndexSum -= (left < 0) ? code[n + left] : code[left];  // Handle negative indices using circular indexing

                // 3. Add the element at 'right' to the sum
                right += 1;
                nextKIndexSum += code[right];  // Add the element at 'right' to the sum
            }
        }

        return decrypted_Code;  // Return the decrypted code array
    }
};

int main() {
    vector<int> code = {2,4,9,3}; int k = -2;
    Solution sol;
    vector<int> decrypted_Code = sol.decrypt(code, k);
    for(const int& x: decrypted_Code)
        cout << x << " ";
    cout << endl;
}