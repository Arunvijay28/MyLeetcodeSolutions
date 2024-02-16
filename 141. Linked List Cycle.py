class linkedlist:
     def __init__(self,val):
          self.val=val
          self.next=None


def hasCycle(self, head) -> bool:
        visit=set()
        current=head
        while current:
            if current in visit:
                return True
            visit.add(current)
            current=current.next
        return False


