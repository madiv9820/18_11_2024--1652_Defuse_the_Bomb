- ## Approach 1:- Brute Force
    - ### Intuition
        The key challenge in this problem is to decrypt a circular array based on a given key `k`, where each element in the array needs to be replaced by the sum of a certain number of its neighboring elements. The circular nature of the array means that when we reach the end of the array, we can "wrap around" to the beginning, and similarly, when accessing elements before the first index, we should wrap to the last element.

    - ### Circular Behavior:
        To handle the circular nature of the array:
            - We use the modulo operator to wrap indices around when accessing elements beyond the array's bounds. For example, for an index `i`, `i % n` will return an index in the range `[0, n-1]`, effectively wrapping around if `i` exceeds `n-1`.
            - For __python__, it can handle negative indices, so we do not need to take care it.

    - ### Approach
        1. **Input Parameters**:
            - `code`: A vector representing the circular array.
            - `k`: An integer key that determines how many elements should be summed.
        2. **Steps**:
            1. **Initialization**:
                - Create an empty array `decrypted_Code` initialized with zeros of the same size as `code`.
            2. **Handling Different Values of `k`**:
                - **When `k == 0`**:
                    - Return an array filled with zeroes as no elements should be summed.          
                - **When `k > 0`**:
                    - Iterate over each index in the array.
                    - For each index, sum the next `k` elements, using modulo `n` to wrap around if necessary.            
                - **When `k < 0`**:
                    - Similarly, iterate over each index.
                    - For each index, sum the previous `|k|` elements, using modulo `n` to wrap around negative indices.
            3. **Return the Decrypted Code**:
                - After processing all elements, return the `decrypted_Code` array.
        3. **Edge Case**:
            - Handle `k == 0` by directly returning an array of zeroes, as no sums are required.

    - ### Code Implementation
        - **Python Solution**

            ```python3 []
            class Solution:
                def decrypt(self, code: List[int], k: int) -> List[int]:
                    # Step 1: Get the length of the code array (size of the circular array)
                    n = len(code)
                    
                    # Step 2: Initialize an empty array `decrypted_Code` with zeros to store the decrypted values
                    decrypted_Code = [0] * n

                    # Step 3: Handle the case when k > 0 (sum the next k elements)
                    if k > 0:
                        for index in range(n):  # Iterate through each index in the original code array
                            nextKIndexSum = 0  # Initialize a variable to accumulate the sum of the next k elements
                            
                            # Determine the start and end indices to sum the next k elements (wrapping around using modulo)
                            start, end = index + 1, index + k
                            
                            # Loop through the next k elements and sum them (wrapping around the array using modulo n)
                            for nextIndex in range(start, end + 1):  # The end is inclusive, hence the +1
                                nextKIndexSum += code[nextIndex % n]  # Use modulo n to ensure circular access to the array

                            # Store the sum of the next k elements in the decrypted_Code at the current index
                            decrypted_Code[index] = nextKIndexSum

                    # Step 4: Handle the case when k < 0 (sum the previous |k| elements)
                    elif k < 0:
                        for index in range(n):  # Iterate through each index in the original code array
                            nextKIndexSum = 0  # Initialize a variable to accumulate the sum of the previous |k| elements
                            
                            # Determine the start and end indices to sum the previous |k| elements (wrapping around using modulo)
                            start, end = index - 1, index + k

                            # Loop through the previous |k| elements and sum them (wrapping around the array using modulo n)
                            for nextIndex in range(start, end - 1, -1):  # Loop backwards from start to end (exclusive)
                                nextKIndexSum += code[nextIndex % n]  # Use modulo n to ensure circular access to the array

                            # Store the sum of the previous |k| elements in the decrypted_Code at the current index
                            decrypted_Code[index] = nextKIndexSum

                    # Step 5: Return the final decrypted code
                    return decrypted_Code
            ```
        
        - **C++ Solution**

            ```cpp []
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
            ```

    - ### Time Complexity
        - **Outer Loop**: We iterate over each element in the array once, so this takes **O(n)** time, where `n` is the size of the input array `code`.
        - **Inner Loop**: For each element, the inner loop sums `|k|` adjacent elements. In the worst case, this could take **O(|k|)** time.
        - Therefore, the total time complexity is **O(n * |k|)**, where `n` is the size of the array and `|k|` is the absolute value of `k`.
        - __Time Complexity Breakdown:__
            - **O(n)**: Iterating over each element in the array.
            - **O(|k|)**: Summing `k` or `|k|` adjacent elements for each index.

        Thus, the total time complexity is **O(n * |k|)**.

    - ### Space Complexity
        - **Space for the Result Array**: We use an additional array `decrypted_Code` of size `n` to store the decrypted values.
        - **Auxiliary Space**: We only use a few extra variables (like counters for loops), which do not depend on the input size.
        - __Space Complexity Breakdown:__
            - **O(n)**: Space for the result array `decrypted_Code`.
            - **O(1)**: Constant space for auxiliary variables (e.g., `nextKIndexSum`, `start`, `end`).

        Thus, the space complexity is **O(n)**, where `n` is the size of the input array `code`.