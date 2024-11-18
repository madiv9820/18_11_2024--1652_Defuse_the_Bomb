# [1652. Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb)

__Type:__ Easy <br>
__Topics:__ Array, Sliding Window <br>
__Companies:__ Amazon
<hr>

You have a bomb to defuse, and your time is running out! Your informer will provide you with a __circular__ array `code` of length of `n` and a key `k`.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

- If `k > 0`, replace the <code>i<sup>th</sup></code> number with the sum of the __next__ `k` numbers.
- If `k < 0`, replace the <code>i<sup>th</sup></code> number with the sum of the __previous__ `k` numbers.
- If `k == 0`, replace the <code>i<sup>th</sup></code> number with `0`.

As `code` is circular, the next element of `code[n-1]` is `code[0]`, and the previous element of `code[0]` is `code[n-1]`.

Given the __circular__ array `code` and an integer key `k`, return _the decrypted code to defuse the bomb_!
<hr>

### Examples:

- __Example 1:__ <br>
__Input:__ code = [5,7,1,4], k = 3 <br>
__Output:__ [12,10,16,13] <br>
__Explanation:__ Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

- __Example 2:__ <br>
__Input:__ code = [1,2,3,4], k = 0 <br>
__Output:__ [0,0,0,0] <br>
__Explanation:__ When k is zero, the numbers are replaced by 0.

- __Example 3:__ <br>
__Input:__ code = [2,4,9,3], k = -2 <br>
__Output:__ [12,5,6,13] <br>
__Explanation:__ The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the __previous__ numbers.
<hr>

### Constraints:
- `n == code.length`
- `1 <= n <= 100`
- `1 <= code[i] <= 100`
- `-(n - 1) <= k <= n - 1`
<hr>

### Hints:
- As the array is circular, use modulo to find the correct index.
- The constraints are low enough for a brute-force solution.