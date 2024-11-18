from typing import List

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
    
if __name__ == '__main__':
    code, k = [2,4,9,3], -2
    sol = Solution()
    print(sol.decrypt(code, k))