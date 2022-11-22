# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://www.youtube.com/watch?v=gBTe7lFR3vc

class Solution:
    def hasCycle(self, head) :
        tortoise, hare = head, head
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        
        return False
    
#  JS solution   
# var hasCycle = function(head) {
#     let hare = head
#     let tortoise = head
    
#     while(hare && hare.next){
#         hare = hare.next.next
#         tortoise = tortoise.next
#         if(hare.val === tortoise.val){
#             return true
#         }
#     }
#     return false     
# };
        
#  My JS 1st wrong Solution:       
# var hasCycle = function(head) {
#     let hare = head.next.next
#     let tortoise = head.next
    
#     while(hare && hare.next){
#         if(hare.val === tortoise.val){
#             return true
#         }
#     }
#     return false     
# };