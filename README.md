# Defuse the Bomb (All Approaches)
- ## Problem Intuition
    The problem asks us to "decrypt" a code using a circular array, where we sum a certain number of elements in the array starting from each index, based on the value of `k`. The key operations depend on whether `k` is positive or negative.

    - **When `k > 0`**: We sum the next `k` elements in the circular array, starting from the index after the current one.
    - **When `k < 0`**: We sum the previous `|k|` elements in the circular array, starting from the index before the current one.
    - **For both cases**, we need to use a sliding window technique to efficiently calculate the sum for each index, moving one step forward and adjusting the sum dynamically.

    The challenge lies in ensuring that the __"circular"__ nature of the array is handled properly, particularly when the indices move beyond the array bounds. This is accomplished using modulo operations. Since python can be handle negative indices, so we don't have to take care of it.

- ## Approach 1:- Brute Force
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