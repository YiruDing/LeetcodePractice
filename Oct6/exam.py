# /*
# Given a string and a number n, replace every nth 
# character with '_'.
# "foreigner", 2 => "f_r_i_n_r"
# "leetcode", 3 => "le_tc_de"
# "leetcode", 1 => "________"
# */

def a(string,number):
    res=''
    n=number
    for i in range(len(string)):
        while n:
            res.append(string[1])
            n-=1
        n=number
    return res

a("foreigner", 2 )

# /*
# Write a function where given a string, it returns 
# the string in reverse except for the characters 
# contained within { }.
 
# input -> output
# "ab{cd}efg" -> "gfecdba"
# "ab{cd}ef{gh}i" -> "ighfecdba"
# */
def b(str):
    res=''
    i=0
    while i<len(str):
        currentRes=''
        if str[i]!="{":
            currentRes.appedn(str[i])
        elif str[i]=='{':
            res.append(currentRes)
        elif str[i]=='}':
            res.append(str[i+1])
    return res        
        
# /*
# Given an array of integers nums, half of the integers 
# in nums are odd, and the other half are even.Sort the 
# array so that whenever nums[i] is odd, i is odd, and 
# whenever nums[i] is even, i is even. Return any answer 
# array that satisfies this condition.
 
# Example 1:
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have 
# been accepted.

# Example 2:
# Input: nums = [3,2]
# Output: [2,3]
# */
def c(arr):
    res=[]
    for i in range(len)
# /*
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a 
# to b (inclusive). Return the smallest sorted list 
# of ranges that cover all the numbers in the array 
# exactly. That is, each element of nums is covered 
# by exactly one of the ranges, and there is no 
# integer x such that x is in one of the ranges but 
# not in nums. Each range [a,b] in the list should 
# be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
# */
