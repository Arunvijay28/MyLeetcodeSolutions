def reverseList(self, head):
        if head is None or head.next is None:
           return head
        prev=None
        curr=head
        while curr:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        head=prev
        return head




