# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 and list2: return list2
        l=ListNode()
        l.next=list1
        ucu=list1
        utemp=l
        lcu=list2
        ltemp=list2
        while lcu and ucu:
            if ucu.val>lcu.val:
                utemp.next=lcu
                ltemp=ltemp.next
                lcu.next=ucu
                lcu=ltemp
                utemp=utemp.next
            else:
                utemp=ucu
                ucu=ucu.next
        if lcu and utemp:
            utemp.next=lcu
        return l.next
