class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if it's the start of the sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

    #     JS solution
    # https://www.youtube.com/watch?v=jcNSCcMNzno

    # To be debugged...
    # My JS solution


#     var longestConsecutive = function(nums) {
#     let numSet=new Set(nums)
#     let longest=0

#     for(let i = 0; i< nums.length;i++){
#         let currentNum=nums[i]
#         if(!(nums[i-1] in numSet)){
#             let length=0
#             while((currentNum+length) in numSet){
#                 length+=1
#             }
#             longest=Math.max(longest,length)
#         }return longest

#     }
# };