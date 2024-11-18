from typing import List

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

if __name__ == '__main__':
    code, k = [2,4,9,3], -2
    sol = Solution()
    print(sol.decrypt(code, k))