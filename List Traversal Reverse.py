'''
You are given a list that contains integers. You need to print the elements of the list with in reverse order with a space between them.

Examples:

Input: arr = [54, 43, 2, 1, 5]
Output: 5 1 2 43 54
Explanation: Just traverse in reverse and print the numbers.
Input: arr = [324, 5, 2, 2]
Output: 2 2 5 324
Explanation: Just traverse in reverse and print the numbers.
'''


def listTraversalReverse(arr):
    for item in arr[::-1]:
        print(item, end=" ")
  
