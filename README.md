- ## Approach 2:- Sliding Window
    - ### Approach
        1. **Input Parsing**: 
            - First, we calculate the size of the array `n` and initialize a result array `decrypted_Code` of size `n` with zeros.     
        2. **For `k > 0` (Summing next `k` elements)**:
            - We initialize two pointers, `left` and `right`, to track the range of elements that contribute to the sum.
            - First, we sum the next `k` elements starting from index `1` (right after the current index). We use modulo to handle the circular nature of the array.
            - After that, we slide the window across the array, adjusting the sum dynamically by subtracting the element that leaves the window (on the `left` side) and adding the element that enters the window (on the `right` side).
        3. **For `k < 0` (Summing previous `|k|` elements)**:
            - Similarly, we sum the previous `|k|` elements starting from the last element (`n-1`).
            - Then, we slide the window across the array, adjusting the sum by removing the element that leaves the window (on the `left` side) and adding the element that enters the window (on the `right` side), while handling negative indices with modulo operations.
        4. **Return the Result**: After iterating through all elements, we return the `decrypted_Code` array.

    - ### Code Implementation

        - **Python Solution**

            ```python3 []
            class Solution:
                def decrypt(self, code: List[int], k: int) -> List[int]:
                    n = len(code)  # Get the length of the code array
                    decrypted_Code = [0] * n  # Initialize the result array with zeroes
                    nextKIndexSum = 0  # This will store the sum of the next k elements (or previous |k| elements)

                    # Case 1: k > 0 (sum the next k elements)
                    if k > 0:
                        left = right = 1  # Start by summing the next k elements; right starts at index 1 (the first element to the right)
                        
                        # Sum the next k elements
                        for _ in range(k):
                            nextKIndexSum += code[right % n]  # Add the element at 'right' to the sum, with circular behavior
                            right = (right + 1) % n  # Move 'right' to the next element, wrapping around if necessary

                        # Now slide the window for each index in the code array
                        for index in range(n):
                            decrypted_Code[index] = nextKIndexSum  # Set the sum at the current index in the decrypted_Code
                            
                            # Slide the window: 
                            # 1. Remove the element at 'left' (the leftmost element in the window) from the sum
                            nextKIndexSum -= code[left]
                            left = (left + 1) % n  # Move 'left' to the next position, wrapping around if necessary
                            
                            # 2. Add the element at 'right' (the next element to the right of the window) to the sum
                            nextKIndexSum += code[right]
                            right = (right + 1) % n  # Move 'right' to the next position, wrapping around if necessary

                    # Case 2: k < 0 (sum the previous |k| elements)
                    elif k < 0:
                        left = right = -1  # Start by summing the previous |k| elements; right starts at the last element of the array
                        
                        # Sum the previous |k| elements (absolute value of k)
                        for _ in range(-k):  # Use abs(k) because we're dealing with negative k
                            nextKIndexSum += code[left]  # Add the element at 'left' to the sum
                            left -= 1  # Move 'left' backwards to the previous element

                        # Now slide the window for each index in the code array
                        for index in range(n):
                            decrypted_Code[index] = nextKIndexSum  # Set the sum at the current index in the decrypted_Code
                            
                            # Slide the window: 
                            # 1. Move 'left' forward to the next element (since it's currently pointing to one before the current window)
                            left = left + 1
                            
                            # 2. Remove the element at the new 'left' position from the sum
                            nextKIndexSum -= code[left]
                            
                            # 3. Add the element at 'right' to the sum
                            right = right + 1
                            nextKIndexSum += code[right]

                    return decrypted_Code  # Return the decrypted code array
            ```
        
        - **C++ Solution**

            ```cpp []
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
            ```

    - ### Time Complexity
        The time complexity of the algorithm is **O(n)**, where `n` is the length of the input array `code`. 

        - We perform an initial summing loop of `|k|` elements (which takes `O(k)` time).
        - Then, we perform a loop over all `n` indices, each time updating the sum in constant time.
        - As a result, the overall time complexity is linear with respect to the size of the array.

    - ### Space Complexity
        The space complexity is **O(n)**, where `n` is the length of the input array `code`.

        - We use an additional array `decrypted_Code` of the same size as the input array to store the result.
        - The space used by other variables (like `left`, `right`, and `nextKIndexSum`) is constant, i.e., `O(1)`, but the space for the result array dominates.