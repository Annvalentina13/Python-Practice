"""
Given a list arr[], of positive integers, and an integer sum. The task is to check if any pair exists in the array whose sum is equal to the given sum. If such a pair exists return true, otherwise, return false.

Example:

Input: arr[] = [1, 2, 3, 3, 5], sum = 8 
Output: true
Explanation: Pair with sum 8 is present in the array which is (3, 5).
Input: arr[] = [3, 2, 5], sum = 6 
Output: false
Explanation: No such pair exists in the array.
Constraints:
1 <= arr.size() <= 104
1 <= arr[i], sum <= 104
"""

def pair_sum(arr, sum):
    seen = set()
    
    for num in arr:
        target = sum - num
        
        if target in seen:
            return True
        
        seen.add(num)
    
    return False
