"""
Remove duplicates in a linked list by having a hash table
We traverse the link list from head to end. For every newly encountered element,
we check whether it is in the hash table: if yes, we remove it; otherwise
we put it in the hash table.
"""

# delete node in linked list when we know that node only
'''
node.val = node.next.val
node.next = node.next.next
'''

# remove nth node from end of linked list
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(head):
            count = 0
            while (head != None):
                head = head.next
                count += 1
            return count
        if head is None:
            return None
        if head.next == None:
            del head
            return None
        temp = head
        count = length(head)
        k = count-n
        if k==0:
            return temp.next
        while k > 1:
            k -= 1
            head = head.next
        head.next = head.next.next
        return temp
'''
# merge two sorted linked lists
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge( h1, h2):
            if h1 is None:
                return h2
            if h2 is None:
                return h1
            if h1.val < h2.val:
                h1.next = merge(h1.next, h2)
                return h1
            else:
                h2.next = merge(h1, h2.next)
                return h2
        k=merge(list1,list2)
        return k
'''

# merge k sorted linked lists
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def SortedMerge(a, b):
            result = None  
            if a is None:
                return b
            elif b is None:
                return a
            if a.val <= b.val:
                result = a
                result.next = SortedMerge(a.next, b)
            else:
                result = b
                result.next = SortedMerge(a, b.next)
            return result
        def merge(arr, last): 
            while (last != 0):
                i = 0
                j = last
                while (i < j):
                    arr[i] = SortedMerge(arr[i], arr[j])  
                    i += 1
                    j -= 1             
                    if (i >= j):
                        last = j
            return arr[0]
        if len(lists)==0:
            return
        arr=[lists[i] for i in range(len(lists))]
        k=len(lists)
        head = merge(arr, k - 1)
        return head
'''

# sort linked list
'''
        if not head:
            return None
        
        # convert linked list to python list
        l = []
        while head: # O(n)
            l.append(head)
            head = head.next
        
        # sort python list by node values
        l.sort(key = lambda x: x.val) # O(nlogn)
        
        # re-link nodes by order in value-sorted python list
        for i in range(0, len(l) - 1): # O(n)
            l[i].next = l[i + 1]
        
        l[-1].next = None # set last node to point to none
        return l[0] # return head
'''