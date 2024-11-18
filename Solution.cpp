#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        // Step 1: Get the size of the input code array
        int n = code.size();
        
        // Step 2: Initialize a vector to store the decrypted code, initially filled with zeroes
        vector<int> decrypted_Code(n, 0);

        // Step 3: Handle the case when k is positive (replace each element with the sum of the next k elements)
        if(k > 0) {
            // Loop through each element in the original code array
            for(int index = 0; index < n; ++index) {
                int nextKIndexSum = 0;  // Initialize a variable to accumulate the sum of the next k elements

                // The start is the next index, and the end is the current index + k (for the sum of next k elements)
                int start = index + 1, end = index + k;

                // Loop to sum the next k elements (use modulo n to handle circular behavior)
                for(int nextIndex = start; nextIndex <= end; ++nextIndex) {
                    nextKIndexSum += code[nextIndex % n];  // Use modulo n to wrap around when the index exceeds the array size
                }
                
                // Store the sum in the decrypted_Code array at the current index
                decrypted_Code[index] = nextKIndexSum;
            }
        }
        // Step 4: Handle the case when k is negative (replace each element with the sum of the previous |k| elements)
        else if(k < 0) {
            // Loop through each element in the original code array
            for(int index = 0; index < n; ++index) {
                int nextKIndexSum = 0;  // Initialize a variable to accumulate the sum of the previous |k| elements

                // The start is the previous index, and the end is the index + k (for the sum of previous |k| elements)
                int start = index - 1, end = index + k;

                // Loop to sum the previous |k| elements (use modulo n to handle circular behavior)
                for(int nextIndex = start; nextIndex >= end; --nextIndex) {
                    // If the nextIndex goes below 0 (wrap around the array), add n to nextIndex before accessing the array
                    nextKIndexSum += ((nextIndex < 0) ? code[n + nextIndex] : code[nextIndex]);
                }

                // Store the sum in the decrypted_Code array at the current index
                decrypted_Code[index] = nextKIndexSum;
            }
        }

        // Step 5: Return the final decrypted code
        return decrypted_Code;
    }
};

int main() {
    vector<int> code = {2,4,9,3}; int k = -2;
    Solution sol;

    vector<int> decrypted_code = sol.decrypt(code, k);
    for(const int& x: decrypted_code)
        cout << x << " ";
    cout << endl;
}