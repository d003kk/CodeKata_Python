class link:
    def __init__(self, next, val):
        self.next =  next
        self.val = val
    def value(self):
        return self.val

class SingleLinkedList:
    """ A singley linked list containing strings """
    def __init__(self):
        self.root = link(None, "")
        pass
        
    def find(self, val):
        lnk = self.root
        while True:
            if lnk.val == val: 
                return lnk
            if lnk.next == None:
                return None;
            lnk = lnk.next
        
    def add(self, val):
        lnk = self.root
        while True:
            if lnk.val == "": 
                lnk.val = val
                return
            elif lnk.next == None:
                lnk.next = link(None, val)
                return None;
            lnk = lnk.next

    def values(self):
        lnk = self.root
        res =[]
        while True:
            res.append(lnk.val)
            if lnk.next == None:
                return res;
            lnk = lnk.next

        
    def delete(self, val):
        if self.root.val == val:
            if self.root.next == None:
                self.root.val = ""
            else:
                self.root = self.root.next
            return
        prev = self.root
        lnk = self.root.next
        if lnk == None:
            return
        while True:
            if lnk.val == val: 
                prev.next = lnk.next
                return
            elif lnk.next == None:
                return
            prev = lnk
            lnk = lnk.next


