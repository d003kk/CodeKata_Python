class link:
    def __init__(self, next, val):
        self.next =  next
        self.val = val
    def value(self):
        return self.val

class SingleLinkedList:
    """ A singley linked list containing strings """
    def __init__(self):
        self.root = None
        pass
        
    def find(self, val):
        lnk = self.root
        while True:
            if lnk == None:
                return None
            if lnk.val == val: 
                return lnk
            lnk = lnk.next
        
    def add(self, val):
        lnk = self.root
        while True:
            if lnk == None: 
                self.root = link(None, val)
                return self.root
            elif lnk.next == None:
                lnk.next = link(None, val)
                return None
            lnk = lnk.next

    def values(self):
        lnk = self.root
        res =[]
        while lnk != None:
            res.append(lnk.val)
            lnk = lnk.next
        return res

        
    def delete(self, delete_me):
        if self.root == delete_me:
            if self.root.next == None:
                self.root = None
            else:
                self.root = self.root.next
            return
        prev = self.root
        lnk = self.root.next
        while True:
            if lnk == None:
                return
            if lnk == delete_me: 
                prev.next = lnk.next
                return
            prev = lnk
            lnk = lnk.next


