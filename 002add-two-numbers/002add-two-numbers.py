# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re=ListNode(0)
        cur=re
        flag=0
        num1=0
        num2=0
        while(l1!=None or l2!=None):
            if l1==None:
                num1=0
            else:
                num1=l1.val
            if l2==None:
                num2=0
            else:
                num2=l2.val
            node=ListNode((num1+num2+flag)%10)
            flag=(num1+num2+flag)/10
            cur.next=node
            cur=node
            if(l1!=None):
              l1=l1.next
            if(l2!=None):
              l2=l2.next
        #最高位进位
        if(flag==1):
            cur.next=ListNode(1)
            cur=cur.next
        cur.next=None
        return re.next
