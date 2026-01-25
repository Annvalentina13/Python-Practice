'''
You are given an array arr[] whose elements form an arithmetic progression (A.P.). Your task is to determine the next three numbers in the progression and return a new array containing the original sequence along with these three additional term.

Examples:

Input: arr[] = ( 1, 5, 9, 13, 17)
Output: 1 5 9 13 17 21 25 29
Explanation: The AP given in array has common difference = 4, therefore next three numbers will be 17+4 = 21, 21+4 = 25, 25+4 = 29. 
Input: arr[] = (3, 1 , -1, -3, -5 , -7)
Output: 3 1 -1 -3 -5 -7 -9 -11 -13
Explanation: The AP given in array has common difference = -2, therefore next three numbers will be -7+(-2) = -9, -9+(-2) = -11, -11+(-2) = -13. 
'''
def extendAP(arr):
    diff = arr[1] - arr[0]
    result = list(arr)

    last = arr[-1]
    for _ in range(3):
        last += diff
        result.append(last)

    return tuple(result)
